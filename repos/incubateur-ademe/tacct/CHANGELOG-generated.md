## Changelog : tacct (30 derniers jours, au 17 août 2026)

### Résumé
Les récentes évolutions se sont concentrées sur l'amélioration de la gestion des comptes utilisateurs, l'enrichissement des contenus et l'optimisation de l'accessibilité. Parallèlement, des travaux techniques importants ont été menés pour stabiliser les bases de données et affiner le suivi analytique du projet.

### Évolutions fonctionnelles
- **Accessibilité** : Amélioration des critères d'accessibilité suite à un audit.
- **Expérience utilisateur** : Ajout du suivi de la dernière date de connexion et correction des accès au compte.
- **Contenus** : Ajout d'un nouvel article sur l'entretien de terrain et réorganisation de l'ordre des articles dans la collection.
- **Interface** : Mise à jour des textes sur la page "Mon Espace" et la bannière de suggestion.

### Évolutions techniques
- **Authentification** : Stabilisation des processus de redirection (déconnexion et URI de redirection) pour le module MonCompteAdeme.
- **Données** : Migration complète de l'historique vers MariaDB et mise à jour du schéma de la base de données.
- **Analytique** : Optimisation du suivi via Posthog (capture de sortie de page, profils utilisateurs et filtrage des navigateurs).
- **Infrastructure & DevOps** : Déploiement de la mise en production du 10 août, gestion des versions Next.js et ajout d'un script de copie de comptes et d'études.

### Autres changements
- **Nettoyage** : Retrait des notifications de maintenance et de certains fichiers de configuration du suivi Git.
