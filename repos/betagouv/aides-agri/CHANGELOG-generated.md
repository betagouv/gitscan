## Changelog : aides-agri (30 derniers jours, au 11 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'administration du site, l'ajout de nouvelles régions géographiques couvertes (Normandie et Bourgogne-Franche-Comté), et des corrections de sécurité et de bugs. Des améliorations de performance ont également été apportées, notamment concernant l'export CSV et la page de résultats.

### Évolutions fonctionnelles
- Ajout de la région Normandie aux zones géographiques prises en charge. [#667](https://github.com/betagouv/aides-agri/issues/667)
- Ajout de la région Bourgogne-Franche-Comté aux zones géographiques prises en charge. [#632](https://github.com/betagouv/aides-agri/issues/632)
- Amélioration de l'administration des retours utilisateurs. [#646](https://github.com/betagouv/aides-agri/issues/646)
- Possibilité de réutiliser les bases juridiques dans l'administration. [#616](https://github.com/betagouv/aides-agri/issues/616)
- Application des filtres lors de l'export CSV des aides depuis l'administration. [#643](https://github.com/betagouv/aides-agri/issues/643)
- Correction du lien vers le formulaire de collecte des aides. [#649](https://github.com/betagouv/aides-agri/issues/649)
- Amélioration de l'affichage des liens externes dans la liste des résultats (ne pas afficher les liens non cliquables). [#629](https://github.com/betagouv/aides-agri/issues/629)
- Comptabilisation des clics vers l'extérieur via les étapes dans la fiche d'aide. [#621](https://github.com/betagouv/aides-agri/issues/621)
- Possibilité d'appliquer les changements d’une fiche mère à tous les niveaux en-dessous d’elle. [#665](https://github.com/betagouv/aides-agri/issues/665)

### Évolutions techniques
- Mise à jour de Django en version 5.2.16. [#666](https://github.com/betagouv/aides-agri/issues/666)
- Migration vers Python 3.14. [#644](https://github.com/betagouv/aides-agri/issues/644)
- Rendre l’export CSV depuis le back-office asynchrone pour améliorer la performance. [#662](https://github.com/betagouv/aides-agri/issues/662)
- Tentative de diminution de l'empreinte mémoire de la page Résultats. [#652](https://github.com/betagouv/aides-agri/issues/652) et [#647](https://github.com/betagouv/aides-agri/issues/647)
- Correction d’une faille de sécurité. [#661](https://github.com/betagouv/aides-agri/issues/661)
- Mise à jour des dépendances (Ruff, pytest, faker, idna, etc.).
- Ajout d'un script pour la création rétroactive des releases Github. [#657](https://github.com/betagouv/aides-agri/issues/657)

### Autres changements
- Mise à jour des CGU et de la politique de confidentialité en vue des alertes mail. [#660](https://github.com/betagouv/aides-agri/issues/660)
- Alerte de l’équipe en cas d’organisme sans logo ayant des aides publiées. [#664](https://github.com/betagouv/aides-agri/issues/664)
- Documentation d'infrastructure : ajout des variables d'environnement. [#633](https://github.com/betagouv/aides-agri/issues/633)
- Correctif sur l'export CSV des aides depuis l'admin. [#656](https://github.com/betagouv/aides-agri/issues/656)
- Correctif du tracking sur les liens externes. [#630](https://github.com/betagouv/aides-agri/issues/630)
- Mise à jour des statistiques pour juin 2026. [#648](https://github.com/betagouv/aides-agri/issues/648)
