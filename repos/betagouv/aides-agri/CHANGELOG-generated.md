## Changelog : aides-agri (30 derniers jours, au 11 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience administrateur, la correction de bugs et l'ajout de nouvelles régions géographiques couvertes par le service. Des améliorations de performance ont également été apportées, notamment concernant l'export CSV et l'affichage des résultats de recherche. Une migration vers Python 3.14 a été réalisée.

### Évolutions fonctionnelles
- Ajout de la région Normandie aux zones géographiques couvertes. [#667](https://github.com/betagouv/aides-agri/issues/667)
- Ajout de la région Bourgogne-Franche-Comté aux zones géographiques couvertes. [#632](https://github.com/betagouv/aides-agri/issues/632)
- Amélioration de l'administration des retours utilisateurs. [#646](https://github.com/betagouv/aides-agri/issues/646)
- Lien direct vers le formulaire de recensement des aides ajouté sur le site. [#638](https://github.com/betagouv/aides-agri/issues/638)
- Possibilité d'appliquer les filtres lors de l'export CSV des aides depuis l'administration. [#643](https://github.com/betagouv/aides-agri/issues/643)
- Les bases juridiques sont maintenant réutilisables dans l'administration. [#616](https://github.com/betagouv/aides-agri/issues/616)
- Correction du lien du formulaire de collecte des aides. [#649](https://github.com/betagouv/aides-agri/issues/649)
- Correction du tracking des liens externes, notamment dans les étapes d'une fiche d'aide. [#630](https://github.com/betagouv/aides-agri/issues/630)
- Les liens non cliquables ne sont plus affichés dans la liste des résultats. [#629](https://github.com/betagouv/aides-agri/issues/629)

### Évolutions techniques
- Migration vers Python 3.14. [#644](https://github.com/betagouv/aides-agri/issues/644)
- L'export CSV depuis le back-office est maintenant asynchrone, améliorant la réactivité de l'interface. [#662](https://github.com/betagouv/aides-agri/issues/662)
- Tentative de réduction de l'empreinte mémoire de la page des résultats de recherche. [#652](https://github.com/betagouv/aides-agri/issues/652) et [#647](https://github.com/betagouv/aides-agri/issues/647)
- Application des changements d’une fiche mère à tous les niveaux d’aides en-dessous. [#665](https://github.com/betagouv/aides-agri/issues/665)
- Correction d'une faille de sécurité. [#661](https://github.com/betagouv/aides-agri/issues/661)
- Mise à jour de plusieurs dépendances (Django, sentry-sdk, pytest, etc.).

### Autres changements
- Alerte envoyée à l’équipe en cas d’organisme sans logo ayant des aides publiées. [#664](https://github.com/betagouv/aides-agri/issues/664)
- Mise à jour des CGU et de la politique de confidentialité en vue des alertes mail. [#660](https://github.com/betagouv/aides-agri/issues/660)
- Ajout de documentation concernant les variables d'environnement pour l'infrastructure. [#633](https://github.com/betagouv/aides-agri/issues/633)
- Script de création rétroactive des releases Github. [#657](https://github.com/betagouv/aides-agri/issues/657)
- Mise à jour des statistiques pour juin 2026. [#648](https://github.com/betagouv/aides-agri/issues/648)
- Correction d'un bug sur l'export CSV des aides depuis l'admin. [#656](https://github.com/betagouv/aides-agri/issues/656)
