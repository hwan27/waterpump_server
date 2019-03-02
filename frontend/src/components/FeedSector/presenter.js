import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.module.scss";

const FeedSector = props => (
  <div className={styles.feed}>
    <ul>
      <Sector title={props.title} />
      {props.map(sector => (
        <Sector title={sector.title} key={sector.id} />
      ))}
    </ul>
  </div>
);

const Sector = props => (
  <li>
    <span>{props.title}</span>
  </li>
);

FeedSector.propTypes = {
  title: PropTypes.string,
  sector_set: PropTypes.arrayOf(
    PropTypes.shape({
      title: PropTypes.string,
      pump_set: PropTypes.arrayOf(PropTypes.shape({ title: PropTypes.string }))
    })
  )
};

export default FeedSector;
