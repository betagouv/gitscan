## Changelog : ui-kit (30 derniers jours, au 07/10/2026)

### Résumé
Cette période est marquée par l'enrichissement des composants de mise en page avec l'ajout de bannières, une amélioration de l'accessibilité des onglets et une gestion plus fluide des droits d'accès aux dossiers. L'outil de documentation (Storybook) a également été rendu plus ergonomique pour les développeurs.

### Évolutions fonctionnelles
- **Mise en page et bannières** : ajout du composant `HeaderBanner` et intégration d'un emplacement (`slot`) pour une bannière supérieure dans le `MainLayout`.
- **Amélioration des composants** :
    - `Tabs` : ajout de variantes accessibles et de la possibilité de contrôler la sélection.
    - `Modal` : correction de problèmes de mise en page.
- **Gestion des accès et partage** :
    - Simplification de l'état des modales de partage et de la confirmation des changements d'accès aux dossiers.
    - Amélioration de l'aperçu (`preview`) pour afficher immédiatement l'absence d'accès sans tenter de charger le contenu.

### Évolutions techniques
- **Optimisation des performances** : ajout d'un mécanisme de *debounce* sur l'écouteur d'événements de redimensionnement pour améliorer la réactivité de l'interface.
- **Amélioration de Storybook** : ajout d'un sélecteur de thème et persistance de la langue sélectionnée lors de la navigation entre les histoires et la documentation.

### Autres changements
- Nettoyage du fichier `CHANGELOG`.
