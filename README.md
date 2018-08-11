# ![image9](https://user-images.githubusercontent.com/26172160/43996133-f2e9687c-9dd9-11e8-80a3-c3bc35304f4e.jpg)

# ESDC_IntelCup2018        

The project was presented in ESDC_IntelCup-2018 held at SJTU,Shanghai,China. The competition theme was AI and IOT, with that 
in mind the project provided a solution that could assist fire-fighters in after fire situation (when the fire is out).  
Many fire-fighters death occur every year due to fire. Our solution Dehazes and cleans the input frames for higher level 
computer vision task like person-detection. Apart from that our solution will give the 3-d map of the location for better 
judging the harm caused at the rescue site. To detect potential person alive victims on the resuce site motion magnification 
is employed on the person detected frame. All the details methioned above are live streamed to the rescue site using 
FLASK (Python Library) server on the local area network.

Intelligent Rescue Operation Bot (IROB) is the implementation of the idea that we propose. As could be seen in the 
image(below) the bot has Kinetic V2 Xbox One(Depth camera), RGB-Camera, Intel Movidius NCS (inference stick provide hardware 
acceleration for deep learning models on embedded platform)and Intel Up-Square as main hardwares apart from other peripherals.  

This repository only contains the frame processing part where the frames for the resuce site is dehazed and 
then person detection is applied on it. 

For dehazing and person-detection we used the state of art algorithms. The RGB image provided by the RGB camera could 
process dehazing and person-detection on UP-Square board. Both dehazing and person-detection was implemented using CNN 
approach (All the details related to the model used could be found in the link below). We used pre-trained models to 
prototype the idea. For dehazing IROB uses AOD-Net and for person-detection MobileNet_SSD (Integration of MobilNet and SSD) 
is used. MobileNet suits the purpose better here than the other state of art methods like YOLO due to its light weight 
and better compatibility with embedded platforms. Intel Movidus NCS does the inferencing to perform the person detection task.




## IROB (Intelligent Rescue Operation Bot)

![alt text](https://lh3.googleusercontent.com/ejcULQwJ1ZZsuvG5xHEy65s-uCvuA6YLKJAP_PO4QK_eJ9KHMq8XpJqlTGcqgTsTxuydhf-BUig-iyJrMDX3dMqyDW9dTbQvEvi8TpezVxr2dxrxSdmiu58vvll9ByKmUGcR6IWhdE4lrCD40y7pk8XltRC8sBD6gfwf1P7-2l8XD8L0pYpT7RE6YzcZgWvVWmaYM_HR2tTvM269IAq-7QAt0LgVEs9B2QuMcOSJThyrdWUM8iATp5JTdM2luuIyStDfUp1tE5y0SAT6CJhrCduCij4bOTnWTDrDEHzlJKH9s51SXqrcUGT_u6bx9RBqECBMHlr9I3I8Pq4NYivyKuhZ5x6fiNlOovKdoxSE-8qqLkDyUDXdVGdFJfvX5_UARBHSn-BqOeDoBhZ5t0u3KGYvPrz6nwpS0563LZELE_nr5muR9vvyuNccRYmjsJGBeZI7btLonnuv_E1WGHlTDl0otxvVkvmVDNOsg6vKTqOW84y-9hUjBOrUtY3hHVCdrZ15uTvn49tRgZC0KpJaerzvcIc7JYDkavjRKA3FsTBjAEV_QanJsgzAx63sklMgOwhZu_ZOyNtvwyi5Z61EpswVps-jYsJj=w720-h959-no)
![alt text](https://lh3.googleusercontent.com/5aROYT3vFOgEQ_qEP6dtq2I_tg-1zstYW8eNJLT4YtSdWDNeCUgWVZK5yxJoZuG53MCNFD3rp--ylpbcWJ39jwvc-voiF8UF8Fib-FbzXLC40fnhGVe9eWRDMeZiQ1E9BTLTgnBh16Fi0GX1IB0nCOd8qFxMGgh0Xb2jePNKcLbSEwtD65-uI1IT4MliRgJWUEbGBc8kpO7y8SPI2mRc8okH4M8CSuIVf6rTisNkNaqwvPsh2ARL3Ems3RY62rrZEzwfd012SWMp-_I5F-53hFrfuwaTmeJ7kma2fGuJvEdaelxgw93Dj_h3wfrRJjQtNw6f_s0hQhTiAanCD1pte9QZz0tiI1OTGJ18A6maGXCH3djVPzBA8Bu1BuwCPy3JOWA8TiGxOSziZftR6WFYKC1D59AFN6P8Xc5twrZLiv_xEtrhjFFQkFAtGXhrZe7RaTKELhW3FAAuOgYuC_gYQdCSIEDy81n4ab8CP__j8iWr0bCqHwXXJ5f-tNk5IkMh4myQyFWNizWRfca0e2f2OTuRynZL6NrW9DAa-1ozt4S2hChH0pZAjdRzYejb-4ngezByLZCJWKcyr0OKb99EJAc56OVt7NRO=w683-h910-no)
## For more details and Algorithms

AOD-Net(All-in-One Dehazing Network) - https://ieeexplore.ieee.org/document/8237773/ 

MobileNet - https://arxiv.org/abs/1704.04861 

SSD (Single Shot MultiBox Detector) - https://www.cs.unc.edu/~wliu/papers/ssd.pdf

Intel Movidius NCS - https://developer.movidius.com/ 

Up-Square Board - http://www.up-board.org/upsquared/

YOLO - https://pjreddie.com/darknet/yolo/

