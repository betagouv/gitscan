## Changelog : mutafriches (30 derniers jours, au 29 mai 2026)

### Résumé
Ce mois-ci, mutafriches a connu des avancées significatives dans l'enrichissement des données et des algorithmes utilisés pour l'analyse de mutabilité des friches urbaines. De nouvelles fonctionnalités ont été ajoutées pour intégrer des données externes, notamment concernant le zonage, le fret et le photovoltaïque, ainsi qu'une page dédiée aux partenaires de la CCI 92. Des optimisations techniques ont également été réalisées pour améliorer la robustesse et la performance de l'application.

### Évolutions fonctionnelles
- Ajout d'une page dédiée aux données externes, permettant le monitoring des imports et des APIs externes. [#112](https://github.com/incubateur-ademe/mutafriches/issues/112)
- Intégration des données de zonage et de fret pour une analyse plus précise de la mutabilité. [#100](https://github.com/incubateur-ademe/mutafriches/issues/100)
- Mise à jour de l'algorithme photovoltaïque pour améliorer la simulation et le calcul. [#111](https://github.com/incubateur-ademe/mutafriches/issues/111)
- Ajout d'une page présentant les partenaires de la CCI 92. [#94](https://github.com/incubateur-ademe/mutafriches/issues/94)
- Ajout du modèle et des statistiques EPCI (Établissement Public de Coopération Intercommunale). [#102](https://github.com/incubateur-ademe/mutafriches/issues/102)
- Correction d'un bug sur la page des données externes. [#114](https://github.com/incubateur-ademe/mutafriches/issues/114)

### Évolutions techniques
- Remplacement de `tsnode` par `node` pour une meilleure performance et compatibilité. [#109](https://github.com/incubateur-ademe/mutafriches/issues/109)
- Suppression du wrapper `migrate` pour simplifier le processus de migration de la base de données. [#107](https://github.com/incubateur-ademe/mutafriches/issues/107)
- Désactivation temporaire de l'ITE fret en attendant la validation du Cerema. [#113](https://github.com/incubateur-ademe/mutafriches/issues/113)

### Autres changements
- Mise à jour de certaines dépendances (PostCSS, globals, uuid, axios) pour bénéficier des dernières corrections et améliorations de sécurité. (Mises à jour automatiques par Dependabot)
