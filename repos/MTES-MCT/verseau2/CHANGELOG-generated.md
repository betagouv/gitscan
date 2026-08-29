## Changelog : verseau2 (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois-ci, Verseau2 a principalement évolué sur ses capacités de reporting et l'intégration de nouveaux processus métier, notamment avec l'ajout de contrôles pour les campagnes PFAS. L'expérience utilisateur a été affinée via des améliorations du tableau de bord et une meilleure gestion des réponses de l'interface, tandis que l'infrastructure a été optimisée pour gagner en performance et en fiabilité.

### Évolutions fonctionnelles
- **Reporting et documents** : Amélioration des rapports PDF avec l'ajout des contrôles V1 et un nouveau formatage spécifique pour l'Agent Verseau [#149](https://github.com/MTES-MCT/verseau2/pull/149) [#148](https://github.com/MTES-MCT/verseau2/pull/148).
- **Nouvelles fonctionnalités** : Mise en place des contrôles dédiés aux campagnes PFAS [#131](https://github.com/MTES-MCT/verseau2/pull/131).
- **Intégration de données** : Transmission des identités (nom et prénom) depuis Orion vers le SFTP de Verseau [#151](https://github.com/MTES-MCT/verseau2/pull/151).
- **Expérience utilisateur (UI/UX)** : 
    - Optimisation du tableau de bord (gestion des dates et style des tableaux) [#143](https://github.com/MTES-MCT/verseau2/pull/143).
    - Amélioration de la gestion et de l'affichage des réponses de l'API [#138](https://github.com/MTES-MCT/verseau2/pull/138).
- **Fiabilité des données** : Correction de la normalisation du champ `numeroDepotVerseau1` [#147](https://github.com/MTES-MCT/verseau2/pull/147).

### Évolutions techniques
- **Performance et infrastructure** : Implémentation de la gestion dynamique de la taille du pool de connexions à la base de données [#141](https://github.com/MTES-MCT/verseau2/pull/141).
- **Sécurité et tests** : Ajout de tests de contrôle d'accès et d'autorisation [#145](https://github.com/MTES-MCT/verseau2/pull/145).
- **Backend et API** :
    - Ajout d'un middleware pour l'en-tête de réponse `X-Source` [#150](https://github.com/MTES-MCT/verseau2/pull/150).
    - Amélioration de la journalisation des erreurs de validation via Zod [#146](https://github.com/MTES-MCT/verseau2/pull/146).
    - Correction de la casse des messages d'erreur bloquants.
- **Développement** : Correction du rafraîchissement rapide (fast refresh) de Sentry avec Vite [#139](https://github.com/MTES-MCT/verseau2/pull/139).

### Autres changements
- **Nettoyage** : Suppression des logs de réponse superflus dans la fonction `apiPostFormData`.
