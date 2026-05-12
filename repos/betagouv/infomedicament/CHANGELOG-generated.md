## Changelog : infomedicament (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration des performances du site, notamment en optimisant le temps de chargement des pages et en réduisant la charge sur les serveurs. De nouvelles fonctionnalités ont été ajoutées concernant les interactions médicamenteuses, avec un widget embarquable et une recherche améliorée. Des corrections de sécurité et des améliorations de l'expérience utilisateur ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un widget embarquable pour les interactions médicamenteuses, accessible via l'URL `/interactions/embed` [#212](https://github.com/betagouv/infomedicament/issues/212).
- Amélioration de la recherche et de la présentation des interactions médicamenteuses, incluant la prise en compte des classes de médicaments et des substances.
- Ajout de classes cliniques et gestion des cas "autres..." dans les interactions médicamenteuses.
- Correction de l'affichage des données sur la page "Médicament" [#192](https://github.com/betagouv/infomedicament/issues/192).
- Ajout d'un sitemap.xml avec un test d'intégration associé.
- Mise à jour des menus d'en-tête et de pied de page.

### Évolutions techniques
- Optimisation des performances :
    - Mise en cache des requêtes statiques vers la base de données avec `unstable_cache` pour réduire la charge lors de la génération statique des pages (SSG).
    - Utilisation de `generateStaticParams` pour la génération statique des listes alpha et du glossaire.
    - Optimisation du chargement des polices (Marianne-Regular_Italic préchargée).
    - Suppression de la prélecture (prefetch) sur certains liens pour améliorer les performances.
    - Déplacement de la sanitisation HTML vers la couche de données côté serveur.
    - Utilisation de composants côté serveur pour certaines parties de l'application.
    - Lazy-loading des composants de la vue détaillée des médicaments.
- Refactorisation :
    - Déplacement du code de l'en-tête et du pied de page vers des layouts spécifiques.
    - Extraction de la logique de récupération des badges de niveau dans un module séparé.
    - Remplacement de l'autocomplete MUI par un composant personnalisé.
- Améliorations de la sécurité :
    - Correction d'une vulnérabilité IDOR sur la soumission de notes avancées.
    - Limitation du nombre de requêtes à l'endpoint `/rating`.
- Infrastructure :
    - Mise à jour des scripts d'importation de la base de données PBDM.
    - Amélioration de la configuration du build pour réduire la taille des images de l'application.
    - Reconfiguration du proxy pour gérer le taux de limitation des requêtes.

### Autres changements
- Nettoyage du code et application des suggestions de revue.
- Mise à jour de la documentation.
- Correction de problèmes de style et d'affichage.
- Ajout de tests d'intégration pour la recherche d'interactions.
- Correction de problèmes liés aux titres de pages trop longs.
- Suppression de dépendances inutiles (MUI).
- Amélioration de la gestion des erreurs et des alertes.
- Correction de la sérialisation de l'arbre ATC complet dans les en-têtes de page.
- Ajout de scripts pour faciliter le développement et le déploiement.
