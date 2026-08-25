## Changelog : eva-serveur (30 derniers jours, au 19 août 2026)

### Résumé
Cette période a été marquée par une restructuration importante du code pour mieux séparer les fonctionnalités spécifiques à l'outil Evapro du cœur du système. Parallèlement, l'expérience utilisateur a été affinée grâce à des améliorations de l'interface, une gestion des droits plus précise pour les conseillers et la résolution de plusieurs bugs d'affichage et de génération de documents.

### Évolutions fonctionnelles
- **Gestion des accès et permissions** : 
    - Ajustement des droits pour les utilisateurs Evapro (possibilité de lancer des campagnes sans pouvoir les lire).
    - Rétablissement de l'accès aux campagnes de structure pour les conseillers Evapro.
- **Améliorations de l'interface (UI)** :
    - Optimisation de la lisibilité des tableaux (campagnes, bénéficiaires) et de l'affichage des événements.
    - Ajout de fils d'Ariane pour faciliter la navigation et affichage des coordonnées (email/téléphone) sur les pages de structures.
    - Simplification du nommage automatique des campagnes Evapro.
    - Ajout de la colonne "structure" dans l'index des superadministrateurs pour les évaluations Evapro.
- **Corrections de bugs** :
    - Résolution de problèmes d'affichage de données (doublons de bénéficiaires, erreurs de redirection, affichage des coûts et des événements d'abandon).
    - Correction de la génération de fichiers PDF.
    - Suppression du formatage automatique sur les champs de saisie de numéros de téléphone pour éviter les erreurs de saisie.

### Évolutions techniques
- **Refonte de l'architecture** : 
    - Restructuration majeure du modèle `Evaluation` pour isoler les concepts propres à l'application Eva (données sociodémographiques, statuts de suivi, mises en action) et améliorer la maintenabilité du code.
- **Optimisation et maintenance** :
    - Réduction du bruit dans les logs en ignorant les requêtes de bots (scans WordPress/PHP et ASP.NET).
    - Nettoyage du code (suppression de méthodes d'aide inutilisées, de routes obsolètes et de code mort).
    - Refactorisation de la logique de lancement des campagnes et des helpers de vue.

### Autres changements
- **Traductions** : Mise à jour des textes pour les métriques de synthèse Evapro et les messages d'aide (hints) de saisie.
