#include <iostream>
#include <math.h>
#include <functional>

#define STB_IMAGE_IMPLEMENTATION
#define STB_IMAGE_WRITE_IMPLEMENTATION

#include "stb_img.h"
#include "stb_img_write.h"

using namespace std;

//const double M_PI = 3.1415;

struct RGB {
    int r, g, b;

    RGB& operator*=(RGB& px) {
        this->r *= px.r;
        this->g *= px.g;
        this->b *= px.b;
        return *this;
    }

    RGB& operator+=(RGB& px) {
        this->r += px.r;
        this->g += px.g;
        this->b += px.b;
        return *this;
    }
};

template<typename T>
class Pixels {
public:
    Pixels(int h, int w) : h(h), w(w) {
        mat = new T*[h];
        for(int i = 0; i < h; i++) {
            mat[i] = new T[w];
        }
    }

    ~Pixels() {
        for(int i = 0; i < h; i++) {
            delete mat[i];
        }

        delete mat;
    }

	T*& operator[](int x) {
		return mat[x];
	}

    void potencia_2() {
        for(int i = 0; i < h; i++) {
            for(int j = 0; j < w; j++) {
                mat[i][j] *= mat[i][j];
            }
        }
    }

    void raiz_quadrada() {
        for(int i = 0; i < h; i++) {
            for(int j = 0; j < w; j++) {
                mat[i][j].r = sqrt(mat[i][j].r);
                mat[i][j].g = sqrt(mat[i][j].g);
                mat[i][j].b = sqrt(mat[i][j].b);
            }
        }
    }

    Pixels<RGB>& operator+=(const Pixels<RGB>& param) {
        if(param.h != this->h or param.w != this->w) {
            return *this;
        }

        for(int i = 0; i < h; i++) {
            for(int j = 0; j < w; j++) {
                this->mat[i][j] += param.mat[i][j];
            }
        }

        return *this;
    }

	int h, w;
private:
    T** mat;
};

// RGB
class image {
public:
    #define channel 3

    image(uint8_t* src, int h, int w) : h(h), w(w), img(h, w) {
        for(int i = 0; i < h; i++) {
            for(int j = 0; j < w; j++) {
                img[i][j] = { src[channel*i*w+(channel*j)], 
                              src[channel*i*w+(channel*j+1)], 
                              src[channel*i*w+(channel*j+2)] };
            }
        }
    }

    image(int h, int w) : h(h), w(w), img(h, w) {
    }

    void image_pura(uint8_t* dest) {
        for(int i = 0; i < h; i++) {
            for(int j = 0; j < w; j++) {
                dest[(channel*j+0)+i*w*channel] = img[i][j].r;
                dest[(channel*j+1)+i*w*channel] = img[i][j].g;
                dest[(channel*j+2)+i*w*channel] = img[i][j].b;
            }
        }
    }

    Pixels<RGB>& get_image() {
        return img;
    }

    int h, w;
private:
    Pixels<RGB> img;
};

// KERNEL DE GAUSS
double filtro_gaus[3][3];

double filto_x[3][3] = {
    1, 0, -1,
    2, 0, -2,
    1, 0, -1
};

double filtro_y[3][3] = {
    1, 2, 1,
    0, 0, 0,
    -1, -2, -1
};

double kernel_laplace[3][3] = {
    0, -1, 0,
    -1, 4, -1,
    0, -1, 0
};

void gerar_filtro_do_gaus() {
    double aux = 2.0, sum = 0.0;

    for(int i = -1; i < 2; i++) {
        for(int j = -1; j < 2; j++) {
            filtro_gaus[i+1][j+1] = exp(-(i*i + j*j) / aux) / (M_PI*aux);
            sum += filtro_gaus[i+1][j+1];
        }
    }

    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            filtro_gaus[i][j] /= sum;
        }
    }
}

image convolucao(image& img, double kernel[3][3]) {
    int h = img.h;
    int w = img.w;

    image out(h, w);
    
    for(int i = 0; i < h; i++) {
        for(int j = 0; j < w; j++) {
            int r = 0, g = 0, b = 0;

            for(int x = 0; x < 3; x++) {
                for(int y = 0; y < 3; y++) {
                    r += img.get_image()[(i-3/2+x + h) % h][(j-3/2+y + w) % w].r * kernel[x][y];
                    g += img.get_image()[(i-3/2+x + h) % h][(j-3/2+y + w) % w].g * kernel[x][y];
                    b += img.get_image()[(i-3/2+x + h) % h][(j-3/2+y + w) % w].b * kernel[x][y];
                }
            }

            out.get_image()[i][j] = { r, g, b };
        }
    }

    return out;
}

void thresholding(image& img) {
	Pixels<RGB>& src = img.get_image();

	double comparator = 10; 

	for(int i = 0; i < img.h; i++) {
		for(int j = 0; j < img.w; j++) {
			RGB c = src[i][j];
			double intensity = (c.r + c.g + c.b) / 3.f;
            if(intensity >= comparator)
                src[i][j] = RGB{255, 255, 255};
            else
                src[i][j] = RGB{0, 0, 0};
		}
	}
}

int main() {
    int largura, altura, canal;

    uint8_t* imagem_rgb = stbi_load("Salen.png", &largura, &altura, &canal, 3);

    image img(imagem_rgb, altura, largura);

    gerar_filtro_do_gaus();
    
    // filtro de Gaus
    image temp = convolucao(img, filtro_gaus);
    
    // sobel
    image img_x = convolucao(temp, filto_x);
    image img_y = convolucao(temp, filtro_y);
    img_x.get_image().potencia_2();
    img_y.get_image().potencia_2();
    img_x.get_image() += img_y.get_image();
    img_x.get_image().raiz_quadrada();
    
    // thresholding
    thresholding(img_x);
    
    // laplace
    image temporario = convolucao(img_x, kernel_laplace);

    temporario.image_pura(imagem_rgb);

    stbi_write_png("Salen_saida.png", largura, altura, 3, imagem_rgb, largura * 3);
    stbi_image_free(imagem_rgb);
    return 0;
}
