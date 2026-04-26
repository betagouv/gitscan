## Changelog : aides-agri (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface d'administration pour la gestion des aides, notamment en permettant la duplication d'aides et en affinant l'organisation des informations. Des corrections de sécurité importantes ont également été apportées pour protéger les données utilisateurs et prévenir les vulnérabilités. Enfin, de nombreuses dépendances ont été mises à jour pour bénéficier des dernières corrections et améliorations.

### Évolutions fonctionnelles
- **Gestion des aides :** Possibilité de dupliquer une aide existante depuis l'interface d'administration. [#448](https://github.com/betagouv/aides-agri/issues/448)
- **Interface d'administration :** Réorganisation des champs dans l'interface d'administration d'une aide pour une meilleure ergonomie. [#446](https://github.com/betagouv/aides-agri/issues/446)
- **Base juridique des aides :** Consolidation et amélioration de la gestion de la base juridique des aides. [#499](https://github.com/betagouv/aides-agri/issues/499) et [#495](https://github.com/betagouv/aides-agri/issues/495)
- **Édition des aides :** Améliorations de l'outil d'édition des aides dans l'interface d'administration. [#498](https://github.com/betagouv/aides-agri/issues/498)
- **Correction d'un bug :** Correction d'un problème de duplication d'aide dans l'interface d'administration. [#449](https://github.com/betagouv/aides-agri/issues/449)
- **Correction d'un bug :** Correction d'un problème de slug des aides. [#497](https://github.com/betagouv/aides-agri/issues/497)

### Évolutions techniques
- **Sécurité :** Correction d'une vulnérabilité d'open-redirection. [#441](https://github.com/betagouv/aides-agri/issues/441) et [#442](https://github.com/betagouv/aides-agri/issues/442)
- **Sécurité :** Mise en place d'une surveillance des attaques par force brute. [#440](https://github.com/betagouv/aides-agri/issues/440)
- **Sécurité :** Obfuscation des données personnelles dans la base de données après l'envoi d'un email. [#439](https://github.com/betagouv/aides-agri/issues/439)
- **Dépendances :** Mises à jour de nombreuses dépendances (Django, Sentry, Faker, Ruff, etc.) pour bénéficier des dernières corrections et améliorations de sécurité.
- **CI/CD :** Optimisation du workflow Github. [#467](https://github.com/betagouv/aides-agri/issues/467)
- **Dépendances :** Correction du système de cooldown des dépendances uv. [#470](https://github.com/betagouv/aides-agri/issues/470)

### Autres changements
- **Documentation :** Ajout de tests pour l'export CSV dans l'interface d'administration. [#438](https://github.com/betagouv/aides-agri/issues/438)
- **Stats :** Ajout des statistiques pour le mois de mars 2026. [#477](https://github.com/betagouv/aides-agri/issues/477)
- **Amélioration :** Déplacement de l'information légale en bas de la page Aide. [#466](https://github.com/betagouv/aides-agri/issues/466)
- **Scripts :** Ajout de scripts pour la création et l'association des logos des DDT(M). [#493](https://github.com/betagouv/aides-agri/issues/493)
- **Fonctionnalité :** Possibilité de créer une fiche mère à partir de plusieurs fiches filles. [#469](https://github.com/betagouv/aides-agri/issues/469)
- **Fonctionnalité :** Modification d'une fiche mère met à jour automatiquement ses fiches filles. [#468](https://github.com/betagouv/aides-agri/issues/468)
