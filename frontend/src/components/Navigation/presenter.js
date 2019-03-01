import React from "react";
import styles from "./styles.module.scss";

const Navigation = (props, context) => (
  <body>
    <div className={styles.header_top}>
      <div className={styles.header_column1} />
      <div className={styles.header_column2}>
        <div className={styles.header_title}>상수도 가압장 관측 제어 설비</div>
      </div>
      <div className={styles.header_column3}>
        <div className={styles.manager_setting}>
          <img
            className={styles.mIcon}
            src={require("images/managerSetting_btn.png")}
          />
          {/* <a href="managerSetting.html">
                    <img className="mIcon" src="images/managerSetting_btn.png">
                </a> */}
        </div>
      </div>
    </div>

    <div className={styles.header_bottom}>
      <div className={styles.header_bottom_column1} />
      <div className={styles.header_bottom_column2}>
        <div className={styles.townPlus}>
          <img
            className={styles.Plus_btn}
            src={require("images/townPlus_btn.png")}
          />
          {/* <a href=""></a>
        <img class="Plus_btn" src="images/townPlus_btn.png"> */}
        </div>
      </div>
    </div>
  </body>
);

export default Navigation;
