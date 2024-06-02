
export type FRAME_IMG = {
    title: string;
    src: string;
    style: string;
    cropp_size: string;
}[][]


export type USER_INFO = {
    design_num: string;
    capture_imgs: string[];
    select_imgs_num: number[];
    made_img: string;
    cropp_size: string;
}

export type MADE_DATE = {
    title: string;
    select_imgs: string[]
}

export type COLLAGE_IMG_DATE = {
    img_name: string;
    collage_img: string;
}