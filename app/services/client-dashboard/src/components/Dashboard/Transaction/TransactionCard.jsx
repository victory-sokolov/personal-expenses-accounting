import React, { useState } from 'react';
import styled from 'styled-components';

const Card = styled.div`
    width: 100%;
    margin: 20px 0 20px;
    background-color: #fff;
    box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
    border-radius: 5px;
    max-width: 100%;
    padding: 26px;

    .transaction-short-details {
        display: flex;
    }

    .left-column {
        margin-left: auto;
    }

    .price {
        font-size: 1.5rem;
    }

    .transaction-details {
        align-items: center;
        justify-content: center;

        img {
            max-width: 200px;
            max-height: 250px;
        }
    }

    .order p {
        font-size: 1.4rem;
        line-height: 5px;
    }

    .arrow {
        border: solid #848282;
        border-width: 0 3px 3px 0;
        display: inline-block;
        padding: 4px;
        margin-left: 10px;
        position: relative;
        bottom: 4px;
        cursor: pointer;
        transform: rotate(45deg);
    }

    .arrow-down {
        transform: rotate(45deg);
        animation-name: arrow-down;
        animation-duration: 1s;
        animation-fill-mode: forwards;
    }

    .arrow-up {
        transform: rotate(-135deg);
        animation-name: arrow-up;
        animation-duration: 1s;
        animation-fill-mode: forwards;
    }

    @keyframes arrow-down {
        from {
            transform: rotate(45deg);
        }
        to {
            transform: rotate(-135deg);
        }
    }

    @keyframes arrow-up {
        from {
            transform: rotate(-135deg);
        }
        to {
            transform: rotate(45deg);
        }
    }
`;

export default function TransactionCard() {

    const [ isActive, setActive ] = useState(false);

    const toggle = () => {
        setActive(!isActive);
    };

    return (
        <div>
            <Card>
                <div className="transaction-short-details">
                    <div className="order">
                        <p>Cafe Holiday</p>
                        <date>29 Feb 2020</date>
                    </div>
                    <div className="left-column">
                        <p class="price">$49.99
                            <i className={isActive ? 'arrow arrow-down' : 'arrow arrow-up'} onClick={toggle}></i>
                        </p>
                    </div>
                </div>

                <div className="transaction-details">
                    {
                        isActive &&
                        <>
                            <img src="" alt="" />
                            <h1>Hiden content</h1>
                        </>

                    }
                </div>
            </Card>


        </div>
    );
}