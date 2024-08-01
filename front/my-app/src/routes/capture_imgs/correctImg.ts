// 보정 기본 값
let exposure = 1.3; // 노출: 이미지 전체의 밝기를 조정.
let brightness = 1.0; // 휘도: 픽셀의 밝기를 조정
let highlights = 1.0; // 하이라이트 : 밝은 영역의 조정을 담당
let contrast = 1.0; // 대비 (contrast): 이미지의 명암 대비를 조정.
let saturation = 1.0; // 채도 (saturation): 색상의 강도를 조정
let hue = 0.0; // 색상 (hue): 색의 종류를 회전시키며 조정
let luminosity = 1.0; // 명도 (luminosity): 이미지의 밝기를 조정
let warmth = 0.5; // 따뜻함 (warmth): 색온도를 조정

export const adjustImage = (imageData: ImageData) => {
    let data = imageData.data;

    for (let i = 0; i < data.length; i += 4) {
        let [r, g, b] = [data[i], data[i + 1], data[i + 2]];

        // 노출 조정
        r *= exposure;
        g *= exposure;
        b *= exposure;

        // 밝기 조정
        r *= brightness;
        g *= brightness;
        b *= brightness;

        // 하이라이트 조정 (간단한 예시)
        if (r > 200 || g > 200 || b > 200) {
            r *= highlights;
            g *= highlights;
            b *= highlights;
        }

        // 대비 조정
        let contrastFactor = (259 * (contrast + 255)) / (255 * (259 - contrast));
        r = clamp(contrastFactor * (r - 128) + 128);
        g = clamp(contrastFactor * (g - 128) + 128);
        b = clamp(contrastFactor * (b - 128) + 128);

        // 채도 조정
        let [h, s, l] = rgbToHsl(r, g, b);
        s *= saturation;
        [r, g, b] = hslToRgb(h, s, l);

        // 색상 조정
        h = (h + hue) % 360;
        [r, g, b] = hslToRgb(h, s, l);

        // 명도 조정
        r *= luminosity;
        g *= luminosity;
        b *= luminosity;

        // 따뜻함 조정 (간단한 예시, 주로 색온도를 이동)
        r += warmth * 10;
        b -= warmth * 10;

        // 클램핑 및 적용
        data[i] = clamp(r);
        data[i + 1] = clamp(g);
        data[i + 2] = clamp(b);
    }
};

const clamp = (value: number) => Math.min(255, Math.max(0, value));

const rgbToHsl = (r: number, g: number, b: number): [number, number, number] => {
    // Normalize the RGB values to the range [0, 1]
    r /= 255; g /= 255; b /= 255;
    
    let max = Math.max(r, g, b);
    let min = Math.min(r, g, b);
    let h: number, s: number, l = (max + min) / 2;

    // Initialize h to avoid uninitialized variable errors
    h = s = 0;

    if (max !== min) {
        let d = max - min;
        s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
        
        switch (max) {
            case r:
                h = (g - b) / d + (g < b ? 6 : 0);
                break;
            case g:
                h = (b - r) / d + 2;
                break;
            case b:
                h = (r - g) / d + 4;
                break;
        }
        h /= 6;
    }

    return [h * 360, s, l];
};


const hslToRgb = (h: number, s: number, l: number) => {
    let r: number, g: number, b: number;

    if (s == 0) {
        r = g = b = l; // 무채색
    } else {
        let hue2rgb = (p: number, q: number, t: number) => {
            if (t < 0) t += 1;
            if (t > 1) t -= 1;
            if (t < 1 / 6) return p + (q - p) * 6 * t;
            if (t < 1 / 2) return q;
            if (t < 2 / 3) return p + (q - p) * (2 / 3 - t) * 6;
            return p;
        }
        let q = l < 0.5 ? l * (1 + s) : l + s - l * s;
        let p = 2 * l - q;
        h /= 360;
        r = hue2rgb(p, q, h + 1 / 3);
        g = hue2rgb(p, q, h);
        b = hue2rgb(p, q, h - 1 / 3);
    }

    return [r * 255, g * 255, b * 255];
}