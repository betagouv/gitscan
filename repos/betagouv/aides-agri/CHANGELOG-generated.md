## Changelog : aides-agri (30 derniers jours, au 2026-04-13)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'administration des aides, avec de nouvelles fonctionnalités pour la duplication et la modification des fiches, ainsi que l'ajout d'export CSV pour les tables de référence. Des corrections de sécurité importantes ont également été apportées, notamment concernant les vulnérabilités open-redirection et la protection contre les attaques par force brute. Enfin, de nombreuses dépendances ont été mises à jour pour assurer la stabilité et la sécurité de l'application.

### Évolutions fonctionnelles
- **Administration des aides :** Possibilité de dupliquer une aide existante depuis l'interface d'administration. [#448](https://github.com/betagouv/aides-agri/issues/448)
- **Administration des aides :** Modification d'une fiche mère met à jour automatiquement ses fiches filles. [#468](https://github.com/betagouv/aides-agri/issues/468)
- **Administration des aides :** Possibilité de créer une fiche mère à partir de plusieurs fiches filles. [#469](https://github.com/betagouv/aides-agri/issues/469)
- **Administration des aides :** Réorganisation des champs dans le formulaire d'édition d'une aide. [#446](https://github.com/betagouv/aides-agri/issues/446)
- **Export de données :** Ajout de la possibilité d'exporter les données de toutes les tables de référence au format CSV. [#424](https://github.com/betagouv/aides-agri/issues/424)
- **Amélioration de la recherche :** Correction du filtre d'aides par zone géographique. [#423](https://github.com/betagouv/aides-agri/issues/423)
- **Mentions légales :** Ajout d'une mention de non-opposabilité sur les fiches d'aides. [#432](https://github.com/betagouv/aides-agri/issues/432)
- **Impression :** Correction de la mise en page lors de l'impression de la recommandation. [#425](https://github.com/betagouv/aides-agri/issues/425)

### Évolutions techniques
- **Sécurité :** Correction d'une vulnérabilité open-redirection. [#441](https://github.com/betagouv/aides-agri/issues/441) et [#442](https://github.com/betagouv/aides-agri/issues/442)
- **Sécurité :** Mise en place d'une surveillance des attaques par force brute. [#440](https://github.com/betagouv/aides-agri/issues/440)
- **Sécurité :** Obfuscation des données personnelles dans la base de données après l'envoi d'un email. [#439](https://github.com/betagouv/aides-agri/issues/439)
- **CI/CD :** Optimisation du workflow GitHub. [#467](https://github.com/betagouv/aides-agri/issues/467)
- **CI/CD :** Mise à jour des actions GitHub pour éviter les avertissements liés à Node.js 20. [#436](https://github.com/betagouv/aides-agri/issues/436)
- **Dépendances :** Mise à jour de nombreuses dépendances (Django, Sentry, requests, etc.) pour bénéficier des dernières corrections et améliorations de sécurité.

### Autres changements
- **Statistiques :** Ajout des statistiques pour le mois de mars 2026. [#477](https://github.com/betagouv/aides-agri/issues/477)
- **Documentation :** Déplacement de l'information légale en bas de la page Aide. [#466](https://github.com/betagouv/aides-agri/issues/466)
- **Tests :** Ajout de tests pour l'export CSV dans l'administration. [#438](https://github.com/betagouv/aides-agri/issues/438)
- **Amélioration du script de mise à jour des dépendances :** Amélioration du script `upgrade-deps`. [#435](https://github.com/betagouv/aides-agri/issues/435)
