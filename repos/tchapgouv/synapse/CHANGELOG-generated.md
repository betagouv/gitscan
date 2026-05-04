## Changelog : synapse (30 derniers jours, au 28 avril 2026)

### Résumé
Cette version apporte des améliorations à la gestion des utilisateurs avec l'introduction d'un répertoire utilisateur basique, des corrections de bugs concernant les tentatives de verrouillage et la validation des événements, ainsi que des optimisations de la configuration et de la gestion de la mémoire cache. L'expiration des comptes utilisateurs est également activée avec MAS.

### Évolutions fonctionnelles
- Introduction d'un répertoire utilisateur basique, permettant une gestion améliorée des utilisateurs. [#4](https://github.com/tchapgouv/synapse/issues/4)
- Activation de l'expiration des comptes utilisateurs via MAS (Matrix Application Services). [#5](https://github.com/tchapgouv/synapse/issues/5)

### Évolutions techniques
- Correction d'un bug concernant l'intervalle de tentatives de verrouillage.
- Augmentation de la taille maximale du corps des requêtes pour résoudre un problème de validation Pydantic lors de la création d'événements. [#17035](https://github.com/tchapgouv/synapse/issues/17035)
- Configuration ajoutée pour exclure certaines salles des mises à jour d'état de profil.
- Optimisation du cache d'introspection MAS, avec une durée de vie de 20 minutes.
- Publication d'un artefact pour l'environnement de développement. [#1](https://github.com/tchapgouv/synapse/issues/1)

### Autres changements
- Correction d'un problème où le gel d'un événement provoquait des erreurs de validation Pydantic.
