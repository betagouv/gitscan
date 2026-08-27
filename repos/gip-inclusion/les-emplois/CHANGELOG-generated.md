## Changelog : les-emplois (30 derniers jours, au 27 août 2026)

### Résumé
Ce mois a été marqué par un développement important du module d'insertion, notamment avec la gestion détaillée des orientations et leur synchronisation avec Dora. L'expérience de gestion des candidats a été enrichie par de nouveaux filtres de recherche, tandis que le processus de candidature a été sécurisé par des contrôles plus stricts sur les dates de contrat.

### Évolutions fonctionnelles
- **Module Insertion & Orientations** : 
    - Ajout d'une vue détaillée pour les orientations et gestion des pièces jointes associées.
    - Mise en place de nouveaux filtres de recherche (expéditeurs, structures, statut, bénéficiaires).
    - Amélioration de la synchronisation des statuts d'orientation depuis Dora.
- **Gestion des Candidats** : 
    - Ajout de nouveaux filtres de recherche (Handicap, fin de parcours IAE imminente, acteurs IAE).
    - Meilleure visibilité des informations de contact des conseillers et alertes lors de la mise à jour de profils avec identité certifiée.
- **Processus de Candidature** : 
    - Renforcement des contrôles sur les dates d'embauche et ajout de composants d'aide à la saisie pour les dates de contrat.
    - Priorisation des liens externes pour les services de diagnostic lors des orientations.
- **Interface & Administration** : 
    - Ajout d'une carte "Mon Récap" dans le tableau de bord des partenaires.
    - Amélioration de l'interface d'administration (affichage des noms d'employés, association des orientations aux événements de mobilisation, gestion des commentaires sur les PASS annulés).
    - Mise à jour des liens vers les formulaires de mise à jour de données ProConnect.

### Évolutions techniques
- **Optimisation des performances** : 
    - Amélioration significative de la vitesse de chargement des listes de candidats (correction de requêtes N+1).
    - Refactorisation des templates pour favoriser leur réutilisation.
- **Gestion des données** : 
    - Automatisation du remplissage des champs de création et de mise à jour (`created_at`, `updated_at`).
    - Amélioration de la gestion des transferts d'entreprises (maintien des évaluations GEIQ).
    - Optimisation de l'utilisation des scopes pour l'API France Travail.
- **Infrastructure & CI/CD** : 
    - Améliorations de la configuration de la CI/CD (setup-uv) et gestion du middleware pour la redirection vers le nouveau domaine.

### Autres changements
- **Documentation & Sécurité** : 
    - Ajout de documentation concernant l'alternative Podman à Docker.
    - Conseils de sécurité intégrés pour la gestion des mots de passe lors de l'utilisation de l'authentification multi-facteurs (MFA).
    - Nettoyage de code et renommage de variables pour une meilleure clarté métier.
