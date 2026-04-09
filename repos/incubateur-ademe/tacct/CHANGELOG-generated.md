## Changelog : tacct (30 derniers jours, au 9 avril 2026)

### Résumé
Ce mois-ci, tacct a subi une refonte importante de son infrastructure et de son code, avec la suppression de fonctionnalités obsolètes (authentification, sandbox, pages de login) et une simplification générale. Des améliorations ont été apportées aux données concernant les sites de baignade, le confort thermique, les plans d'eau, les populations vulnérables au grand âge, ainsi que les données relatives à l'arbovirose et aux moustiques tigres. Des corrections de bugs et des ajustements de l'interface utilisateur ont également été effectués.

### Évolutions fonctionnelles
- Ajout d'une notice avec une date d'affichage sur la page d'accueil.
- Amélioration des données et de l'affichage des sites de baignade, incluant une migration de la base de données pour la qualité des sites.
- Mise à jour des données relatives au confort thermique.
- Mise à jour des données concernant les plans d'eau et ajout d'événements Posthog associés.
- Intégration des données relatives à l'arbovirose et aux moustiques tigres, avec des améliorations de l'interface utilisateur (texte, responsive design, overlay).
- Correction d'un lien de redirection cassé.
- Correction d'une coquille dans un texte.
- Correction d'un problème d'affichage des données pour les territoires d'outre-mer.
- Ajout d'une notification concernant les données manquantes pour l'arbovirose en outre-mer.

### Évolutions techniques
- Refactorisation du code pour supprimer les fonctionnalités d'authentification, de sandbox et de login.
- Suppression de dossiers et de code inutiles.
- Mise à jour de Prisma.
- Suppression des utilisateurs et de la sandbox dans la base de données.
- Modification de la commande de build.
- Suppression de l'iframe.
- Suppression des tests de la commande de build.
- Mise à jour des packages et du schéma Prisma.
- Override de pnpm pg pour la construction.
- Mise à jour des modèles de la base de données.
- Ajout de tests E2E et Jest.
- Refactorisation des noms de tacct.
- Correction d'une erreur liée à `x-forwarded-host`.
- Installation du lock file.
- Ajout d'un iframe.
- Mise à jour du bucket RGA et de la table grand âge.

### Autres changements
- Ajout d'une notice sur la page d'accueil.
- Refactorisation du robots.txt et du sitemap.
- Suppression de vieux sites de baignade.
- Intégration de textes facilitant l'accessibilité (facili-tacct) dans tacct.
- Merge des branches `facili-tacct` et `main`.
- Merge des branches `arbovirose` et `moustique tigre`.
- Merge des branches `sources des indicateurs` et `grand age`.
- Merge des branches `MAJ plans d'eau + posthog events` et `microdataviz dots + home page + patch DROM + textes facili-tacct en tacct`.
