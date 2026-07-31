## Changelog : aides-agri (30 derniers jours, au 11 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de la région Normandie au catalogue des aides, l'amélioration de la gestion des organismes et des fiches d'aide, ainsi que des corrections de sécurité et d'export de données. Des optimisations de performance ont également été apportées pour réduire l'empreinte mémoire de la page de résultats.

### Évolutions fonctionnelles
- Ajout de la région Normandie aux régions couvertes par le service. [#667](https://github.com/betagouv/aides-agri/issues/667)
- Possibilité d'appliquer les changements d'une fiche mère à toutes les fiches d'aide qui en dépendent. [#665](https://github.com/betagouv/aides-agri/issues/665)
- Alerte envoyée à l'équipe en cas d'organisme sans logo ayant des aides publiées. [#664](https://github.com/betagouv/aides-agri/issues/664)
- Correction du lien vers le formulaire de collecte des aides. [#649](https://github.com/betagouv/aides-agri/issues/649)
- L'export CSV des aides depuis l'interface d'administration est maintenant asynchrone, améliorant la réactivité de l'interface. [#662](https://github.com/betagouv/aides-agri/issues/662)
- Correction d'un bug sur l'export CSV des aides depuis l'admin. [#656](https://github.com/betagouv/aides-agri/issues/656)

### Évolutions techniques
- Mise à jour de Django en version 5.2.16. [#666](https://github.com/betagouv/aides-agri/issues/666)
- Correction d'une faille de sécurité. [#661](https://github.com/betagouv/aides-agri/issues/661)
- Optimisation de l'empreinte mémoire de la page de résultats. [#652](https://github.com/betagouv/aides-agri/issues/652)
- Script de création rétroactive des releases Github pour améliorer la gestion des versions. [#657](https://github.com/betagouv/aides-agri/issues/657)
- Mise à jour des CGU et de la politique de confidentialité en vue des alertes mail. [#660](https://github.com/betagouv/aides-agri/issues/660)

### Autres changements
- Mise à jour des statistiques pour juin 2026. [#648](https://github.com/betagouv/aides-agri/issues/648)
- Mises à jour de dépendances (soupsieve, @sentry/browser, mjml-python, sentry-sdk[django], coverage, ruff, uv).
