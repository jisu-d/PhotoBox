import type { FRAME_IMG } from '$lib/public/type'

export const frameimg: FRAME_IMG = [
    [
        {
            title: '1-1',
            src: '/frame/1/1.jpg',
            style: 'top: -5%;  right: -10%; position: relative; box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px; transition: z-index 0.3s, transform 0.3s ease-in-out; width: 80%; max-width: calc(min(50vh, 50vw));',
            cropp_size: '4:5',
            cover: false
        },
        {
            title: '1-2',
            src: '/frame/1/2.jpg',
            style: 'top: 5%; left: -10%; position: relative; box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px; transition: z-index 0.3s, transform 0.3s ease-in-out; width: 80%; max-width: calc(min(50vh, 50vw));',
            cropp_size: '4:5',
            cover: false
        }
    ],
    [
        {
            title: '2-1',
            src: '/frame/2/1.png',
            style: 'top: -5%;  right: -10%; position: relative; box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px; transition: z-index 0.3s, transform 0.3s ease-in-out; width: 80%; max-width: calc(min(50vh, 50vw));',
            cropp_size: '4:5',
            cover: true
        },
    ],
]


