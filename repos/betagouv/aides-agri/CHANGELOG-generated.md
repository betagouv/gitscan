## Changelog : aides-agri (30 derniers jours, au 2026-04-23)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface d'administration pour faciliter la gestion des aides, notamment la duplication et la modification en masse. Des corrections de sécurité importantes ont également été apportées pour protéger les données utilisateurs et prévenir les vulnérabilités. Enfin, de nombreuses dépendances ont été mises à jour pour bénéficier des dernières corrections et améliorations.

### Évolutions fonctionnelles
- **Gestion des aides :** Possibilité de dupliquer une aide existante depuis l'interface d'administration. [#448](https://github.com/betagouv/aides-agri/issues/448)
- **Gestion des aides :** Possibilité de modifier une fiche mère et de propager les changements à ses fiches filles. [#468](https://github.com/betagouv/aides-agri/issues/468)
- **Gestion des aides :** Réorganisation des champs dans l'interface d'administration pour une meilleure ergonomie. [#446](https://github.com/betagouv/aides-agri/issues/446)
- **Informations légales :** Ajout d'une mention de non-opposabilité sur les fiches d'aides. [#432](https://github.com/betagouv/aides-agri/issues/432)
- **Export CSV :** Ajout de tests pour l'export CSV dans l'interface d'administration. [#438](https://github.com/betagouv/aides-agri/issues/438)
- **Base juridique :** Consolidation de la notion de base juridique des aides. [#499](https://github.com/betagouv/aides-agri/issues/499) et [#495](https://github.com/betagouv/aides-agri/issues/495)
- **Edition des aides :** Améliorations de l'outil d'édition des aides. [#498](https://github.com/betagouv/aides-agri/issues/498)

### Évolutions techniques
- **Sécurité :** Correction d'une vulnérabilité open-redirection. [#441](https://github.com/betagouv/aides-agri/issues/441) et [#442](https://github.com/betagouv/aides-agri/issues/442)
- **Sécurité :** Implémentation d'une surveillance des attaques brute-force. [#440](https://github.com/betagouv/aides-agri/issues/440)
- **Sécurité :** Obfuscation des données personnelles dans la base de données après envoi d'un email. [#439](https://github.com/betagouv/aides-agri/issues/439)
- **CI/CD :** Optimisation du workflow Github. [#467](https://github.com/betagouv/aides-agri/issues/467)
- **Dépendances :** Mise à jour de nombreuses dépendances (Django, Django-DSFR, Sentry, Faker, Ruff, etc.) pour bénéficier des dernières corrections et améliorations.
- **Scripts :** Scripts de création/association des logos des DDT(M). [#493](https://github.com/betagouv/aides-agri/issues/493)
- **Cooldow dépendances :** Correction du système de cooldown des dépendances uv. [#470](https://github.com/betagouv/aides-agri/issues/470)

### Autres changements
- **Documentation :** Ajout des statistiques de mars 2026. [#477](https://github.com/betagouv/aides-agri/issues/477)
- **Configuration :** Amélioration du script d'upgrade des dépendances. [#435](https://github.com/betagouv/aides-agri/issues/435)
- **CI/CD :** Mise à jour des actions Github pour éviter les warnings nodejs 20. [#436](https://github.com/betagouv/aides-agri/issues/436)
- **Slug :** Correction du slug des aides. [#497](https://github.com/betagouv/aides-agri/issues/497)
