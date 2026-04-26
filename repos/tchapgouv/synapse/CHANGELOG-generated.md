## Changelog : synapse (30 derniers jours, au 25 avril 2026)

### Résumé
Cette mise à jour apporte des améliorations de performance et de stabilité au serveur Synapse, notamment concernant la gestion des verrous, la mise en cache de l'introspection MAS et la gestion des événements. Une nouvelle fonctionnalité permet également d'exclure certaines pièces de la mise à jour de l'état du profil, et l'expiration des comptes est activée avec MAS.

### Évolutions fonctionnelles
- Activation de l'expiration des comptes avec MAS [#5](https://github.com/tchapgouv/synapse/issues/5).
- Possibilité d'exclure certaines pièces de la mise à jour de l'état du profil via une nouvelle configuration [#17035](https://github.com/tchapgouv/synapse/issues/17035).

### Évolutions techniques
- Correction d'un bug concernant l'intervalle de nouvelle tentative de verrouillage.
- Mise en cache de l'introspection MAS avec une durée de 20 minutes.
- Augmentation de la taille maximale du corps de la requête pour corriger un problème de validation Pydantic lors de la création d'événements [#17035](https://github.com/tchapgouv/synapse/issues/17035).
- Publication d'un artefact pour l'environnement de développement [#1](https://github.com/tchapgouv/synapse/issues/1).

### Autres changements
- Aucun changement significatif à signaler.
