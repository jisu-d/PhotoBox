import { writable, type Writable } from 'svelte/store';

import type { USER_INFO } from '$lib/public/type'

export const user_data: Writable<USER_INFO> = writable<USER_INFO>({
    design_num: ' ',
    capture_imgs: [], // 6장의 사진의 데이터를 가진 배열
    select_imgs_num: [], // 배열의 길이가 4개 capture_imgs배열의 이미지 index
    made_img: ' ',
    cropp_size: ' ',
    cover: null,
    printoutNum: 1,
    imgPath: ' ',
});


// count.set(1); // logs '1'
// count.update((n) => n + 1); // logs '2'
// $user_data // 현재 값 불러오기