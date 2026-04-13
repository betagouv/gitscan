## Changelog : synapse (30 derniers jours, au 2026-04-10)

### Résumé
Cette version apporte des améliorations à la gestion des utilisateurs via le service d'authentification Matrix (MAS), notamment la possibilité de verrouiller des comptes. Des optimisations ont été apportées au cache MAS et à la gestion des requêtes. La préparation de la version 1.150.0 est également en cours, avec une release candidate disponible.

### Évolutions fonctionnelles
- Possibilité pour le service MAS de verrouiller le statut d'un utilisateur dans Synapse. [#19554](https://github.com/tchapgouv/synapse/issues/19554)
- Activation de l'expiration des comptes avec MAS. [#5](https://github.com/tchapgouv/synapse/issues/5)
- Augmentation de la taille maximale du corps des requêtes pour résoudre des problèmes de validation Pydantic lors de la création d'événements. [#17035](https://github.com/tchapgouv/synapse/issues/17035)
- Configuration ajoutée pour exclure certaines salles des mises à jour d'état du profil.

### Évolutions techniques
- Optimisation du cache MAS, avec une durée de vie de 20 minutes.
- Migration des dépendances de développement vers des groupes de dépendances PEP 735. [#19490](https://github.com/tchapgouv/synapse/issues/19490)
- Ajout de labels plus clairs aux logs des requêtes traitées. [#19548](https://github.com/tchapgouv/synapse/issues/19548)
- Correction d'un problème dans le CI où l'image complement était pointée vers une image inexistante. [#19523](https://github.com/tchapgouv/synapse/issues/19523)
- Correction de la restauration d'une modification concernant `localhost/complement-synapse`. [#19523](https://github.com/tchapgouv/synapse/issues/19523)
- Mise à jour de la syntaxe des paramètres de chemin dans la documentation de l'API d'administration pour assurer la cohérence. [#19307](https://github.com/tchapgouv/synapse/issues/19307)
- Correction pour que `delay_id` soit placé dans les données non signées pour l'expéditeur (MSC4140). [#19479](https://github.com/tchapgouv/synapse/issues/19479)

### Autres changements
- Préparation de la version 1.150.0 avec une release candidate (1.150.0rc1) disponible.
- Publication d'un artefact pour le développement. [#1](https://github.com/tchapgouv/synapse/issues/1)
- Mises à jour de dépendances : pyopenssl, pyjwt.
