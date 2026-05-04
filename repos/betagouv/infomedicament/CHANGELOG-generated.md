## Changelog : infomedicament (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de nouvelles données (classes cliniques et interactions médicamenteuses), l'optimisation des performances du site (temps de chargement, préchargement) et la correction de failles de sécurité potentielles. Des améliorations de l'expérience utilisateur ont également été apportées, notamment au niveau de la recherche et de l'affichage des informations sur les médicaments.

### Évolutions fonctionnelles

- Ajout des classes cliniques avec le système de classification PATHOS. [#212](https://github.com/betagouv/infomedicament/issues/212)
- Ajout d'un sitemap.xml pour améliorer le référencement du site.
- Implémentation d'une page d'intégration pour les interactions médicamenteuses, permettant de les intégrer sur d'autres sites.
- Ajout de chapeaux et gestion des cas "autres..." pour les classes médicamenteuses.
- Amélioration de la recherche et de la consultation des interactions médicamenteuses, avec la prise en compte des classes et substances.
- Correction de l'affichage de toutes les données sur la page d'un médicament. [#192](https://github.com/betagouv/infomedicament/issues/192)
- Affichage dynamique du nombre de médicaments commercialisés.
- Calcul de la fraîcheur des données affichée dans le modal de bienvenue.

### Évolutions techniques

- Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment concernant les interactions médicamenteuses.
- Optimisation des performances du site :
    - Utilisation de SVGO pour optimiser les SVG de la page d'accueil.
    - Lazy loading des composants de la vue détaillée des médicaments.
    - Désactivation du préchargement dans les liens de l'en-tête et du pied de page.
    - Déplacement de la fonction de sanitisation HTML vers la couche de données côté serveur.
- Suppression de la dépendance à la librairie MUI (Material UI) et remplacement par des composants custom.
- Amélioration de la gestion des scripts d'importation de données pour les environnements de développement et de production (Scalingo).
- Utilisation de TypeScript pour les scripts d'importation de données.
- Amélioration de la sécurité :
    - Correction d'une potentielle faille IDOR (Insecure Direct Object Reference) sur la soumission des évaluations.
    - Limitation du nombre de requêtes à l'endpoint `/rating` pour prévenir les abus.
- Mise en place de tests d'intégration pour la recherche et la consultation des interactions médicamenteuses.
- Amélioration de la configuration du proxy pour limiter le nombre de requêtes par minute.

### Autres changements

- Correction de plusieurs erreurs mineures et améliorations de la qualité du code.
- Mise à jour de la documentation.
- Amélioration de la gestion des titres de pages pour autoriser plus de caractères.
- Correction de l'affichage des alertes DSFR (Design System for Government).
- Ajout d'un flag `isBdm` pour le comptage des spécialités.
