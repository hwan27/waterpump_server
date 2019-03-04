import React from "react";

const Sector = props => (
  <div>
    <ul>
      {props.sectors.map(sector => (
        <Town title={sector.title} key={sector.id} />
      ))}
    </ul>
  </div>
);

const Town = props => (
  <li>
    <span>{props.title}</span>
  </li>
);

export default Sector;
