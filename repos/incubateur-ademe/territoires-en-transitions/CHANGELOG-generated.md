## Changelog : territoires-en-transitions (30 derniers jours, au 26 juin 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment sur la gestion des plans d'action et des preuves, avec une attention particulière portée à la duplication de plans et à la visualisation des données. Des efforts importants ont également été consacrés à la sécurité, à la performance et à la maintenance technique du code. L'import de plans via Excel progresse avec l'implémentation de nouvelles étapes et une gestion plus robuste des données.

### Évolutions fonctionnelles
- Possibilité de dupliquer un plan d'action existant, incluant les budgets, les preuves et les notes associées.
- Amélioration de l'affichage des badges de statut et de priorité des actions dans les tableaux.
- Ajout d'une modale de clôture d'audit en deux étapes pour une meilleure confirmation.
- Les utilisateurs ADEME peuvent désormais télécharger les preuves d'autres collectivités.
- Amélioration de la gestion des statuts des tâches et des actions.
- Ajout d'une fonctionnalité pour verrouiller les preuves de labellisation après validation d'un audit.
- Possibilité de filtrer les actions par statut et priorité dans les vues "Toutes les actions" et "Suivi personnel".
- Amélioration de l'affichage des informations dans le header d'une mesure, avec un affichage "sticky" sur les grands écrans.
- Ajout d'une fonctionnalité pour afficher les scores indicatifs dans les nouvelles sous-mesures.
- Ajout d'une action "Dupliquer l'action" dans les menus de fiche.
- Amélioration de la page "Mesure désactivée" avec une gestion des timeouts et une meilleure synchronisation des données.
- Ajout d'un bandeau pour basculer vers la nouvelle vue de labellisation.

### Évolutions techniques
- Refactorings importants du code, notamment dans les domaines de l'import de plans (AI Plan Import) et de la gestion des labels.
- Amélioration de la sécurité avec des corrections pour bloquer les injections SQL et les attaques de type IDOR.
- Optimisation des performances, notamment en supprimant des dépendances inutiles et en améliorant la gestion des requêtes.
- Mise à jour des dépendances (Next.js, eslint-config-next).
- Suppression de code obsolète et de fichiers inutilisés.
- Utilisation de TypeScript pour améliorer la robustesse du code.
- Amélioration de la gestion des tests, avec migration vers Vitest et correction de tests existants.
- Implémentation d'un client Gemini structuré pour l'IA.
- Refonte de l'éditeur de texte riche (RichTextEditor) pour une meilleure gestion des sauts de ligne.
- Amélioration de la gestion des erreurs et des logs.
- Utilisation de Row-Level Security (RLS) pour restreindre l'accès aux données.

### Autres changements
- Mise à jour de la documentation.
- Amélioration de la gestion des fichiers et des documents.
- Corrections de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout de tests unitaires et d'intégration.
- Amélioration de la structure du projet et de l'organisation du code.
- Ajout de commentaires et de documentation pour faciliter la maintenance du code.
- Synchronisation des données CRM depuis les outils.
- Ajustement des données de test pour une meilleure couverture.
