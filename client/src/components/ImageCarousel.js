import Carousel from 'react-bootstrap/Carousel';

function ImageCarousel() {
    return (
      <Carousel>
        <Carousel.Item>
          <img alt='' src='https://images.unsplash.com/photo-1573493334464-21388936965a?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cGFyayUyMGJlbmNofGVufDB8fDB8fHww' fluid />
          <Carousel.Caption>
            <h3>Parks</h3>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
        <img alt='' src='https://images.unsplash.com/photo-1627927518258-b67557570840?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjZ8fG5laWdoYm9yaG9vZHxlbnwwfDB8MHx8fDA%3D' fluid />
          <Carousel.Caption>
            <h3>Neighborhoods</h3>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
        <img alt='' src='https://images.unsplash.com/photo-1473895908536-7cbe5466790f?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzF8fHBsYXlncm91bmR8ZW58MHwwfDB8fHww' fluid />
          <Carousel.Caption>
            <h3>Amenities</h3>
          </Carousel.Caption>
        </Carousel.Item>
      </Carousel>
    );
  }
  
  export default ImageCarousel;