## Changelog : aides-agri (30 derniers jours, au 11 juillet 2026)

### Résumé
Les récentes mises à jour d'aides-agri améliorent la gestion des aides et des organismes, notamment en étendant la couverture géographique à la Normandie et en permettant la propagation des modifications d'une fiche mère à ses fiches enfants. Des améliorations de performance ont été apportées à l'export CSV et des correctifs de sécurité ont été implémentés.

### Évolutions fonctionnelles
- Ajout de la région Normandie aux régions couvertes par le catalogue d'aides. [#667](https://github.com/betagouv/aides-agri/issues/667)
- Possibilité de propager les modifications d'une fiche mère à toutes les fiches d'aide qui en dépendent. [#665](https://github.com/betagouv/aides-agri/issues/665)
- Alerte envoyée à l'équipe en cas d'organisme sans logo ayant des aides publiées. [#664](https://github.com/betagouv/aides-agri/issues/664)
- L'export CSV des aides depuis l'interface d'administration est désormais asynchrone, améliorant ainsi la réactivité de l'application. [#662](https://github.com/betagouv/aides-agri/issues/662)
- Correction d'une faille de sécurité. [#661](https://github.com/betagouv/aides-agri/issues/661)
- Correction de l'export CSV des aides depuis l'admin. [#656](https://github.com/betagouv/aides-agri/issues/656)

### Évolutions techniques
- Mise à jour de Django en version 5.2.16. [#666](https://github.com/betagouv/aides-agri/issues/666)
- Mise à jour de plusieurs dépendances : `@sentry/browser`, `mjml-python`, `sentry-sdk[django]`, `coverage`, `ruff`.
- Script de création rétroactive des releases Github pour améliorer la gestion des versions. [#657](https://github.com/betagouv/aides-agri/issues/657)
- Verrouillage de la version d'uv. [#655](https://github.com/betagouv/aides-agri/issues/655)

### Autres changements
- Mise à jour des CGU et de la politique de confidentialité en préparation des alertes mail. [#660](https://github.com/betagouv/aides-agri/issues/660)
