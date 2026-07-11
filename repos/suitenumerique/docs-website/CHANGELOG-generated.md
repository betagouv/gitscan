## Changelog : docs-website (30 derniers jours, au 9 juillet 2026)

### Résumé
Ce mois-ci, le site web de Docs a été entièrement repensé et migré vers Astro pour une meilleure performance et une maintenance simplifiée. Le contenu est désormais principalement récupéré en direct depuis le projet Docs lui-même, assurant une cohérence accrue et une mise à jour facilitée. De nouvelles sections ont été ajoutées pour mettre en valeur la communauté, la feuille de route et l'impact du projet.

### Évolutions fonctionnelles
- **Nouvelle page Communauté :** Ajout d'une section "Contributeurs" pour mettre en avant les membres actifs de la communauté.
- **Nouvelle page Appel Communautaires :** Intégration d'une page listant les appels communautaires, alimentée par le contenu de Docs.
- **Nouvelle page Feuille de route :** La feuille de route du projet est désormais accessible via une nouvelle page, avec des sous-pages pour chaque élément de la feuille de route.
- **Amélioration de la navigation :** Remplacement du logo et du texte de la marque par le logo "wordmark" de Docs.
- **Mise à jour des liens GitHub :** Correction des liens vers la documentation GitHub, qui ont été déplacés vers le sous-chemin "documentation".
- **Icône FAQ :** Remplacement de l'icône "plus-in-circle" de la FAQ par une flèche (chevron).
- **Section "Hacker News sensation" :** Ajout d'une section présentant l'historique des étoiles GitHub pour illustrer l'intérêt du projet.
- **Manifeste :** Simplification de la navigation et correction des liens sur la page du manifeste, dont le contenu est maintenant récupéré directement depuis Docs.

### Évolutions techniques
- **Migration vers Astro :** Le site a été migré de son framework précédent vers Astro, améliorant ainsi les performances et la maintenabilité.
- **Récupération de contenu en direct :** Le contenu de la feuille de route et du manifeste est désormais récupéré en direct depuis le projet Docs au moment de la construction du site.
- **Ajout d'un CNAME :** Configuration d'un CNAME pour le domaine personnalisé docs.la-suite.eu.
- **Refactoring du contenu :** Fusion des sections "roadmap-sync" et "blog README" en une seule section "Contenu de Docs".

### Autres changements
- Ajout des fichiers README, LICENSE et CONTRIBUTING.
- Ajout d'un fichier d'intégration pour les nouveaux contributeurs.
- Initialisation du dépôt avec un premier commit.
