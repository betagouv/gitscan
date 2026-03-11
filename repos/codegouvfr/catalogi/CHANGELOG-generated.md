## Changelog : catalogi (30 derniers jours)

### Résumé
Cette mise à jour apporte des améliorations à la robustesse du catalogue, notamment en corrigeant un problème lié à la gestion des liens externes qui pouvaient devenir obsolètes. De plus, des tests automatisés de bout en bout ont été ajoutés pour garantir la qualité et la stabilité de l'application, en particulier dans le contexte d'une authentification via Keycloak.

### Évolutions fonctionnelles
- Correction d'un bug où les liens externes pouvaient devenir invalides lors de la mise à jour des données [#726ce20](https://github.com/codegouvfr/catalogi/commit/726ce20). Le système rebind désormais automatiquement ces liens.

### Évolutions techniques
- Ajout de tests E2E (End-to-End) avec Playwright, incluant une configuration avec Keycloak et Testcontainers pour des tests plus complets et fiables [#47e483e](https://github.com/codegouvfr/catalogi/commit/47e483e).

### Autres changements
- Mise à jour de la version du projet [#827f2a1](https://github.com/codegouvfr/catalogi/commit/827f2a1).
- Ajout d'un fichier de documentation qui est ignoré par Git [#6dc158a](https://github.com/codegouvfr/catalogi/commit/6dc158a).
