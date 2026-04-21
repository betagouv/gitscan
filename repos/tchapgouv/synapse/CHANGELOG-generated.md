## Changelog : synapse (30 derniers jours, au 16 mai 2026)

### Résumé
Cette version apporte des améliorations de performance et de stabilité, notamment concernant la gestion des verrous et la mise en cache de l'introspection MAS. Des corrections ont été apportées pour résoudre des problèmes de validation d'événements et d'expiration des comptes. Une nouvelle option de configuration permet d'exclure certaines salles des mises à jour d'état de profil.

### Évolutions fonctionnelles
- Activation de l'expiration des comptes via MAS [#5](https://github.com/tchapgouv/synapse/issues/5).
- Ajout d'une option de configuration pour exclure certaines salles des mises à jour d'état de profil [#17035](https://github.com/tchapgouv/synapse/issues/17035).
- Augmentation de la taille maximale du corps des requêtes pour éviter des erreurs de validation.

### Évolutions techniques
- Correction d'un bug concernant l'intervalle de nouvelle tentative de verrouillage.
- Mise en cache de l'introspection MAS avec une durée de 20 minutes.
- Correction d'un problème où le gel d'un événement provoquait des erreurs de validation Pydantic [#1](https://github.com/tchapgouv/synapse/issues/1).
- Publication d'un artefact pour l'environnement de développement.

### Autres changements
- Préparation de la version 1.150.0.
