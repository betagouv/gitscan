## Changelog : france-chaleur-urbaine-publicodes (30 derniers jours)

### Résumé
Les dernières mises à jour du projet se concentrent sur l'amélioration des calculs et des données concernant les systèmes de chauffage, notamment les PAC (Pompes à Chaleur) et le solaire. Une nouvelle version a été publiée (1.4.0) avec des améliorations sur les aides financières pour les solutions collectives. Des ajustements ont également été apportés pour faciliter la publication du projet sur npmjs.

### Évolutions fonctionnelles
- Ajout du bilan sur 1 an pour les PAC hybrides, le solaire thermique et les systèmes solaires combinés (puis annulé par un revert).
- Mise à jour des données pour le gaz individuel (P1). [#issue à investiguer]
- Amélioration des données pour le dimensionnement des PAC.
- Mise à jour des aides pour les solutions collectives à 35%. [#issue à investiguer]
- Ajout de la situation tertiaire moyenne. [#issue à investiguer]

### Évolutions techniques
- Passage à un "trusted publisher" pour la publication sur npmjs, ce qui permet de supprimer le token d'authentification NODE_AUTH_TOKEN.
- Publication de la version 1.3.0 et 1.4.0 du projet.
- Ajout de scripts pour obtenir les tableaux intermédiaires et compléter le script `external-keys` avec les paramètres du simulateur.

### Autres changements
- Documentation mise à jour pour refléter le passage à un "trusted publisher".
