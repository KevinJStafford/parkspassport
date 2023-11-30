import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { RxHamburgerMenu } from "react-icons/rx";
import React, {useState} from "react"
import HamburgerMenu from "./HamburgerMenu";

function Header() {
    return (
        <Navbar expand='lg' className='bg-body-tertiary'>
            <Container>
                <Navbar.Brand className='brand' href="http://localhost:3000">Parks Passport</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto" style={{marginLeft: 'auto'}}>
                        <Nav.Link></Nav.Link>
                        <HamburgerMenu/>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    )
}

export default Header

