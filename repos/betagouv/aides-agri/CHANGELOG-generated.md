## Changelog : aides-agri (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité du site, l'ajout de nouvelles fonctionnalités pour la gestion des aides en back-office (duplication, modification en cascade), et la mise à jour des dépendances pour maintenir la stabilité et la sécurité de l'application. Des corrections de vulnérabilités et des améliorations de l'expérience utilisateur dans l'interface d'administration ont également été apportées.

### Évolutions fonctionnelles
- Possibilité de dupliquer une aide existante depuis l'interface d'administration. [#448](https://github.com/betagouv/aides-agri/issues/448)
- Modification d'une fiche mère d'aide se répercute désormais sur ses fiches filles. [#468](https://github.com/betagouv/aides-agri/issues/468)
- Ajout d'une mention de non-opposabilité sur les fiches d'aides. [#432](https://github.com/betagouv/aides-agri/issues/432)
- Amélioration de la mise en page lors de l'impression de la recommandation. [#425](https://github.com/betagouv/aides-agri/issues/425)
- Ajout de statistiques pour le mois de mars 2026. [#477](https://github.com/betagouv/aides-agri/issues/477)
- Réorganisation des champs dans l'interface d'administration pour la gestion des aides. [#446](https://github.com/betagouv/aides-agri/issues/446)

### Évolutions techniques
- Mise à jour de nombreuses dépendances (Django, Sentry, requests, etc.) pour bénéficier des dernières corrections de sécurité et améliorations de performance.
- Correction de vulnérabilités open-redirection. [#441](https://github.com/betagouv/aides-agri/issues/441) et [#442](https://github.com/betagouv/aides-agri/issues/442)
- Implémentation d'une surveillance des attaques de type brute-force. [#440](https://github.com/betagouv/aides-agri/issues/440)
- Optimisation du workflow GitHub pour une meilleure efficacité. [#467](https://github.com/betagouv/aides-agri/issues/467)
- Correction du système de cooldown des dépendances uv. [#470](https://github.com/betagouv/aides-agri/issues/470)
- Mise à jour de django-dsfr vers la version 3.4.0 [#459](https://github.com/betagouv/aides-agri/issues/459)

### Autres changements
- Obfuscation des données personnelles dans la base de données après l'envoi d'un email. [#439](https://github.com/betagouv/aides-agri/issues/439)
- Ajout de tests pour l'export CSV dans l'interface d'administration. [#438](https://github.com/betagouv/aides-agri/issues/438)
- Amélioration du script de mise à jour des dépendances. [#435](https://github.com/betagouv/aides-agri/issues/435)
- Déplacement de l'information légale en bas de la page Aide. [#466](https://github.com/betagouv/aides-agri/issues/466)
