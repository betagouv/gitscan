## Changelog : aides-agri (30 derniers jours, au 21 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'administration des aides, avec la possibilité de dupliquer des fiches, de modifier les fiches mères et leurs fiches filles, ainsi que des améliorations de l'interface d'administration. Des corrections de sécurité importantes ont également été apportées, notamment pour corriger des vulnérabilités open-redirection et renforcer la protection contre les attaques par force brute. Enfin, de nombreuses dépendances ont été mises à jour pour bénéficier des dernières corrections et améliorations.

### Évolutions fonctionnelles
- Possibilité de dupliquer une aide depuis l'interface d'administration. [#448](https://github.com/betagouv/aides-agri/issues/448)
- Modification d'une fiche mère met à jour automatiquement ses fiches filles. [#468](https://github.com/betagouv/aides-agri/issues/468)
- Création d'une fiche mère à partir de plusieurs fiches filles. [#469](https://github.com/betagouv/aides-agri/issues/469)
- Réorganisation des champs dans l'interface d'administration d'une aide pour une meilleure ergonomie. [#446](https://github.com/betagouv/aides-agri/issues/446)
- Ajout d'une mention de non-opposabilité sur les fiches d'aides. [#432](https://github.com/betagouv/aides-agri/issues/432)
- Ajout de tests pour l'export CSV dans l'interface d'administration. [#438](https://github.com/betagouv/aides-agri/issues/438)

### Évolutions techniques
- Correction de vulnérabilités open-redirection. [#441](https://github.com/betagouv/aides-agri/issues/441) et [#442](https://github.com/betagouv/aides-agri/issues/442)
- Mise en place d'une surveillance des attaques par force brute. [#440](https://github.com/betagouv/aides-agri/issues/440)
- Obfuscation des données personnelles dans la base de données après l'envoi d'un email. [#439](https://github.com/betagouv/aides-agri/issues/439)
- Optimisation du workflow GitHub. [#467](https://github.com/betagouv/aides-agri/issues/467)
- Amélioration du script de mise à jour des dépendances. [#435](https://github.com/betagouv/aides-agri/issues/435)
- Correction d'un problème de "cooldown" des dépendances uv. [#470](https://github.com/betagouv/aides-agri/issues/470)
- Mises à jour de nombreuses dépendances : Django, Django-DSFR, Sentry, Faker, Pygments, Requests, Gunicorn, Ruff, etc.

### Autres changements
- Ajout des statistiques pour le mois de mars 2026. [#477](https://github.com/betagouv/aides-agri/issues/477)
- Déplacement de l'information légale en bas de la page "Aide". [#466](https://github.com/betagouv/aides-agri/issues/466)
- Amélioration de la configuration des actions GitHub pour éviter les avertissements liés à Node.js 20. [#436](https://github.com/betagouv/aides-agri/issues/436)
