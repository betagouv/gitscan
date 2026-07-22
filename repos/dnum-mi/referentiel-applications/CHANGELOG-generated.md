## Changelog : referentiel-applications (30 derniers jours, au 2026-07-21)

### Résumé
Cette version apporte des améliorations significatives à la gestion des droits d'accès, de la recherche, et de l'importation de données. Des corrections d'accessibilité (RGAA) ont également été implémentées. L'interface utilisateur a été améliorée avec l'ajout de nouvelles fonctionnalités comme la gestion des licences et des informations sur les technologies utilisées.

### Évolutions fonctionnelles
- Ajout d'un endpoint pour le catalogue de données et des actions associées en front-end. ([#2024](https://github.com/dnum-mi/referentiel-applications/issues/2024))
- Refonte de la gestion des technologies utilisées par les applications, incluant des informations sur les produits, la documentation et la fin de vie (EOL). ([#2058](https://github.com/dnum-mi/referentiel-applications/issues/2058))
- Ajout de la possibilité de trier les types d'acteurs. ([#1974](https://github.com/dnum-mi/referentiel-applications/issues/1974))
- Amélioration de la recherche globale avec un préfixe et une meilleure fiabilité. ([#2025](https://github.com/dnum-mi/referentiel-applications/issues/2025), [#2030](https://github.com/dnum-mi/referentiel-applications/issues/2030))
- Ajout de tags et de sélections. ([#1992](https://github.com/dnum-mi/referentiel-applications/issues/1992))
- Possibilité de tracer les modifications de la matrice des droits dans l'historique. ([#1899](https://github.com/dnum-mi/referentiel-applications/issues/1899))
- Ajout de la possibilité de modifier globalement les applications en tant qu'administrateur. ([#1888](https://github.com/dnum-mi/referentiel-applications/issues/1888))
- Import Excel des onglets applications et hébergements. ([#752](https://github.com/dnum-mi/referentiel-applications/issues/752), [#1889](https://github.com/dnum-mi/referentiel-applications/issues/1889))
- Import Excel générique avec une feuille Conformités. ([#753](https://github.com/dnum-mi/referentiel-applications/issues/753), [#1881](https://github.com/dnum-mi/referentiel-applications/issues/1881))
- Amélioration de la gestion des droits d'accès : l'administrateur d'une application a désormais tous les droits sur celle-ci. ([#2028](https://github.com/dnum-mi/referentiel-applications/issues/2028), [#2031](https://github.com/dnum-mi/referentiel-applications/issues/2031))
- Ajout de la gestion des tokens applicatifs pour les administrateurs. ([#1939](https://github.com/dnum-mi/referentiel-applications/issues/1939))

### Évolutions techniques
- Fiabilisation du démarrage de la base de données et du backend en CI. ([#2023](https://github.com/dnum-mi/referentiel-applications/issues/2023))
- Amélioration des performances de la recherche d'applications. ([#1975](https://github.com/dnum-mi/referentiel-applications/issues/1975))
- Correction de problèmes de "flakiness" dans les tests E2E. ([#1984](https://github.com/dnum-mi/referentiel-applications/issues/1984))
- Correction de vulnérabilités de sécurité (Dependabot). ([#1904](https://github.com/dnum-mi/referentiel-applications/issues/1904), [#1905](https://github.com/dnum-mi/referentiel-applications/issues/1905))
- Amélioration de la gestion des permissions pour l'import Excel. ([#1890](https://github.com/dnum-mi/referentiel-applications/issues/1890), [#1892](https://github.com/dnum-mi/referentiel-applications/issues/1892))
- Correction de code smells TypeScript (SonarQube). ([#1898](https://github.com/dnum-mi/referentiel-applications/issues/1898), [#1905](https://github.com/dnum-mi/referentiel-applications/issues/1905))
- Amélioration de la gestion des images Docker pour OpenShift. ([#1914](https://github.com/dnum-mi/referentiel-applications/issues/1914))

### Autres changements
- Documentation récapitulative du RefApp et ajout d'ADR (Architecture Decision Records). ([#1634](https://github.com/dnum-mi/referentiel-applications/issues/1634), [#1987](https://github.com/dnum-mi/referentiel-applications/issues/1987))
- Améliorations d'accessibilité (RGAA) : contraste des couleurs, éléments graphiques, formulaires, messages de statut, accessibilité des liens, structure globale des templates, etc. ([#1770](https://github.com/dnum-mi/referentiel-applications/issues/1770), [#1775](https://github.com/dnum-mi/referentiel-applications/issues/1775), [#1776](https://github.com/dnum-mi/referentiel-applications/issues/1776), [#1779](https://github.com/dnum-mi/referentiel-applications/issues/1779), [#1780](https://github.com/dnum-mi/referentiel-applications/issues/1780), [#1782](https://github.com/dnum-mi/referentiel-applications/issues/1782), [#1784](https://github.com/dnum-mi/referentiel-applications/issues/1784), [#1921](https://github.com/dnum-mi/referentiel-applications/issues/1921), [#1922](https://github.com/dnum-mi/referentiel-applications/issues/1922), [#1924](https://github.com/dnum-mi/referentiel-applications/issues/1924), [#1929](https://github.com/dnum-mi/referentiel-applications/issues/1929), [#1930](https://github.com/dnum-mi/referentiel-applications/issues/1930), [#1932](https://github.com/dnum-mi/referentiel-applications/issues/1932), [#1935](https://github.com/dnum-mi/referentiel-applications/issues/1935))
- Suppression de la fonctionnalité de gestion des licences. ([#2057](https://github.com/dnum-mi/referentiel-applications/issues/2057))
- Correction de l'affichage du libellé de statut même sans date. ([#2017](https://github.com/dnum-mi/referentiel-applications/issues/2017), [#2019](https://github.com/dnum-mi/referentiel-applications/issues/2019))
