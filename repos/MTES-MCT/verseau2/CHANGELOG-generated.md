## Changelog : verseau2 (30 derniers jours, au 11/09/2026)

### Résumé
Ce mois-ci, Verseau2 a bénéficié d'améliorations significatives concernant la génération de rapports PDF et l'accessibilité. L'expérience utilisateur a été affinée grâce à une meilleure gestion des messages d'erreur et une interface de tableau de bord optimisée, tandis que l'intégration de données avec Orion a été renforcée.

### Évolutions fonctionnelles
- **Amélioration de l'interface** : Ajustement de la largeur des colonnes du tableau de bord pour une meilleure lisibilité [#160](https://github.com/MTES-MCT/verseau2/issues/160).
- **Accessibilité** : Ajout d'une nouvelle page dédiée à l'accessibilité et à ses liens de support [#158](https://github.com/MTES-MCT/verseau2/issues/158).
- **Reporting** : Enrichissement des rapports PDF avec l'ajout des contrôles V1 et d'un nouveau formatage spécifique pour les agents [#149](https://github.com/MTES-MCT/verseau2/issues/149), [#148](https://github.com/MTES-MCT/verseau2/issues/148).
- **Expérience utilisateur** : Optimisation des messages d'erreur (connexion et erreurs bloquantes) pour une meilleure clarté [#155](https://github.com/MTES-MCT/verseau2/issues/155).
- **Interopérabilité** : Transmission des noms et prénoms depuis Orion vers le SFTP de Verseau [#151](https://github.com/MTES-MCT/verseau2/issues/151).

### Évolutions techniques
- **Configuration** : Ajout d'une option permettant de désactiver l'indexation [#159](https://github.com/MTES-MCT/verseau2/issues/159).
- **Observabilité** : Mise en place de la gestion des sessions de replay Sentry pour faciliter le débogage [#144](https://github.com/MTES-MCT/verseau2/issues/144).
- **Architecture API** : Ajout d'un middleware pour l'en-tête de réponse `X-Source` [#150](https://github.com/MTES-MCT/verseau2/issues/150).
- **Fiabilité des données** : Corrections sur la normalisation du champ `numeroDepotVerseau1` et sur la journalisation des erreurs de validation via Zod [#147](https://github.com/MTES-MCT/verseau2/issues/147), [#146](https://github.com/MTES-MCT/verseau2/issues/146).
