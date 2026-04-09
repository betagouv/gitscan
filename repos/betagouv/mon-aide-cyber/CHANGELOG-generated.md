## Changelog : mon-aide-cyber (30 derniers jours, au 7 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la robustesse de l'application, notamment en corrigeant des erreurs liées à l'API de géolocalisation et à la gestion des diagnostics. Des travaux ont également été menés pour permettre une meilleure gestion des demandes d'aide non pourvues, avec l'ajout de commandes d'administration dédiées. Enfin, une attention particulière a été portée à la sécurité en mettant à jour plusieurs dépendances vulnérables.

### Évolutions fonctionnelles
- Correction d'un bug empêchant la gestion correcte des erreurs renvoyées par l'API Géo lors de la récupération des informations EPCI. [#issue](https://github.com/betagouv/mon-aide-cyber/issues/ef62115)
- Amélioration de la gestion des diagnostics :
    - Retour des diagnostics même en l'absence d'aidant associé. [#issue](https://github.com/betagouv/mon-aide-cyber/issues/7cd0465)
    - Spécification des demandes sans diagnostic. [#issue](https://github.com/betagouv/mon-aide-cyber/issues/d111d74)
- Ajout de commandes d'administration pour faciliter la recherche et le suivi des demandes d'aide non pourvues. [#issue](https://github.com/betagouv/mon-aide-cyber/issues/f7b8398)
- Implémentation de la recherche des aidés. [#issue](https://github.com/betagouv/mon-aide-cyber/issues/dcfd146)
- Initialisation de la recherche des demandes non pourvues. [#issue](https://github.com/betagouv/mon-aide-cyber/issues/d9f291a)
- Les résultats des aides non pourvues sont maintenant enregistrés dans un fichier. [#issue](https://github.com/betagouv/mon-aide-cyber/issues/5cef27c)

### Évolutions techniques
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (minimatch, rollup, immutable, dompurify). [#issue](https://github.com/betagouv/mon-aide-cyber/security/dependabot/128), [#issue](https://github.com/betagouv/mon-aide-cyber/security/dependabot/120), [#issue](https://github.com/betagouv/mon-aide-cyber/security/dependabot/131)
- Correction d'erreurs suite à la mise à jour des dépendances. [#issue](https://github.com/betagouv/mon-aide-cyber/issues/24071ad)
- Passage du UI Kit en version 1.28.4. [#issue](https://github.com/betagouv/mon-aide-cyber/issues/8dd7854)
- Suppression d'un UI Kit non utilisé. [#issue](https://github.com/betagouv/mon-aide-cyber/issues/b676122)

### Autres changements
- Mise à jour des tampons d'homologation MAC. [#issue](https://github.com/betagouv/mon-aide-cyber/issues/06ebd85)
- La commande d'administration pour la recherche des demandes non pourvues a été rendue exécutable. [#issue](https://github.com/betagouv/mon-aide-cyber/issues/3fbf367)
