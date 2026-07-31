## Changelog : mon-service-securise (30 derniers jours, au 30 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration des statistiques et du reporting, avec l'ajout d'une page de statistiques administratives, de graphiques et de données enrichies. Des améliorations significatives ont également été apportées à la gestion des référentiels externes et à la génération de documents, notamment l'implémentation de Typst pour les PDF. Des corrections et des optimisations diverses ont été apportées à l'interface utilisateur et au code.

### Évolutions fonctionnelles
- Ajout d'une page de statistiques pour les administrateurs, incluant des graphiques sur l'évolution du nombre de services et par type de service.
- Possibilité de filtrer les statistiques par type de service.
- Affichage des données des référentiels externes (ReCyf, ISO2700X) dans les listes de mesures et tiroirs.
- Ajout d'une page publique répertoriant toutes les mesures du référentiel V2.
- Implémentation de la première page du PDF "Annexes" en Typst, incluant les risques spécifiques.
- Ajout d'une option pour accepter ou refuser le pixel de suivi dans le parcours d'inscription.
- Amélioration de la recherche textuelle pour inclure les noms des responsables de mesures.
- Ajout d'une page "Documents" et d'une page "Avis".

### Évolutions techniques
- Conversion de plusieurs modèles de données métier en Typescript pour une meilleure typage et maintenabilité.
- Refonte de la gestion des tiroirs, avec conversion du tiroir "Mesure" en un tiroir Svelte.
- Utilisation de Typst pour la génération de documents PDF, remplaçant les anciennes méthodes.
- Amélioration de la gestion des erreurs et des exceptions.
- Mise à jour de nombreuses dépendances.
- Ajout de tests unitaires et d'intégration.
- Optimisation de la performance de certaines requêtes.

### Autres changements
- Amélioration de la documentation et des commentaires dans le code.
- Corrections de style et de mise en page.
- Suppression de code obsolète et de dépendances inutilisées.
- Ajout de nouvelles variables d'environnement et de configurations.
- Amélioration de l'accessibilité de certains composants.
- Ajout de données JSON+LD pour améliorer le référencement.
- Ajout d'un script pour extraire les données ReCyf de Grist.
- Ajout d'un script pour extraire les données ISO2700X du CSV.
