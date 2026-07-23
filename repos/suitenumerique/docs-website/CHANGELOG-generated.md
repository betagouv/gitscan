## Changelog : docs-website (30 derniers jours, au 21 juillet 2026)

### Résumé
Ce mois-ci, le site web de Docs a été entièrement reconstruit avec Astro, permettant de récupérer le contenu directement depuis le projet Docs lui-même. Cela assure une cohérence accrue et une mise à jour plus facile du contenu. Plusieurs pages ont été ajoutées ou améliorées, notamment la feuille de route, le manifeste, les appels communautaires et une section dédiée aux contributeurs.

### Évolutions fonctionnelles
- Ajout d'une page dédiée aux appels communautaires, alimentée par le contenu de Docs.
- Ajout d'une section "Contributeurs" présentant la communauté Docs.
- Ajout d'une section "Hacker News sensation" avec un graphique de l'historique des étoiles GitHub.
- Mise à jour des liens GitHub pour refléter le nouveau chemin `documentation/`.
- Remplacement de l'icône "plus-in-circle" dans la FAQ par une flèche.
- Uniformisation de la terminologie "sub-docs" sur la page d'accueil.
- Ajout d'une feuille de route dynamique, alimentée par le contenu de Docs, avec des sous-pages pour chaque élément de la feuille de route.
- Migration du contenu du manifeste depuis un fichier statique vers une récupération dynamique depuis Docs.

### Évolutions techniques
- Migration complète du site vers Astro.
- Ajout d'un fichier CNAME pour le domaine personnalisé `docs.la-suite.eu`.
- Simplification de la navigation et correction des liens.
- Fusion des sections "roadmap-sync" et "blog README" en une seule section "Contenu de Docs".
- Mise à jour de la source du logo SVG.
- Initialisation du dépôt avec un fichier README, LICENSE et CONTRIBUTING.

### Autres changements
- Ajout d'un fichier d'intégration pour les nouveaux contributeurs.
- Remplacement du logo et du texte de la marque de navigation par le logo "wordmark" de Docs.
