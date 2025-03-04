import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Card from 'react-bootstrap/Card';
import { Link } from 'react-router-dom';

function Grid() {
  return (
    <Container>
      <Row className="justify-content-md-center">
        <Col sm>
          <Link to={'/parks'} className={'normal-text'}>
            <Card className='card' style={{ width: 'auto'}}>
              <Card.Img variant="top" src="https://images.unsplash.com/photo-1573493334464-21388936965a?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cGFyayUyMGJlbmNofGVufDB8fDB8fHww" />
              <Card.Body>
                <Card.Title className="landing-card">Parks</Card.Title>
              </Card.Body>
            </Card>
            </Link>
        </Col>
        <Col sm>
          <Link to={'/neighborhoods'} className={'normal-text'}>
            <Card className='card' style={{ width: 'auto' }}>
              <Card.Img variant="top" src="https://images.unsplash.com/photo-1627927518258-b67557570840?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjZ8fG5laWdoYm9yaG9vZHxlbnwwfDB8MHx8fDA%3D" />
              <Card.Body>
                <Card.Title className="landing-card">Neighborhoods</Card.Title>
              </Card.Body>
            </Card>
          </Link>
        </Col>
        <Col>
          <Link to={'/amenities'} className={'normal-text'}>
            <Card className='card' style={{ width: 'auto' }}>
                <Card.Img variant="top" src="https://images.unsplash.com/photo-1473895908536-7cbe5466790f?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzF8fHBsYXlncm91bmR8ZW58MHwwfDB8fHww" />
                <Card.Body>
                  <Card.Title className="landing-card">Amenities</Card.Title>
                </Card.Body>
            </Card>
          </Link>
        </Col>
      </Row>
    </Container>
  );
}

export default Grid;