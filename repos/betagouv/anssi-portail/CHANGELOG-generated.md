## Changelog : anssi-portail (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration du parcours de sécurisation, notamment avec l'ajout de fonctionnalités pour le module Cyberdépart et la gestion des mesures. Des améliorations significatives ont également été apportées à la performance et à la sécurité du site, ainsi qu'à l'optimisation SEO. Une migration vers le rendu côté serveur (SSR) est en cours pour améliorer la vitesse de chargement et l'accessibilité.

### Évolutions fonctionnelles
- Ajout du parcours complet de sécurisation avec affichage des modules et des mesures associées.
- Mise en avant du module Cyberdépart dans le parcours de sécurisation.
- Affichage du nombre de mesures disponibles.
- Amélioration de l'affichage du site sur différents écrans (large, tablette).
- Ajout d'un toast pour afficher des messages à l'utilisateur.
- Affichage du badge Cyberdépart une fois le module complété.
- Affichage de la progression de l'utilisateur dans le parcours de sécurisation.
- Ajout de liens vers des mesures plus avancées.
- Correction de l'affichage des pages "services".
- Amélioration de l'affichage des cartes DSFR.
- Ajout des pages de contacts régionaux et des mesures associées.
- Mise à jour des liens canoniques et ajout du fichier sitemap.xml pour améliorer le SEO.
- Ajout des données structurées d'indexation pour le SEO.
- Correction de l'URL canonique pour inclure le 'site.url'.

### Évolutions techniques
- Migration progressive vers le rendu côté serveur (SSR) pour améliorer la performance et le SEO.
- Utilisation de UUID v7 pour la génération de clés primaires.
- Refonte de la configuration d'Axios pour une meilleure gestion des requêtes.
- Amélioration de la gestion des erreurs et des logs.
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité et améliorer la stabilité (dompurify, @babel/core, vite, form-data, shell-quote).
- Ajout d'un Nix Shell pour faciliter le développement en local.
- Renforcement de la sécurité des workflows CI/CD.
- Utilisation de nouveaux outils de validation de configuration (zizmor).
- Centralisation de la gestion de la configuration et des chemins.
- Amélioration de la structure du code et suppression de code inutile.
- Ajout de tests Playwright pour l'automatisation des tests d'intégration.

### Autres changements
- Mise à jour de la documentation.
- Correction de petites erreurs de wording et de style.
- Ajout de commentaires et de documentation pour améliorer la lisibilité du code.
- Amélioration de la gestion des secrets dans les workflows CI/CD.
- Ajout de métadonnées Open Graph et Twitter pour le partage sur les réseaux sociaux.
- Ajout du fichier robots.txt pour le contrôle de l'indexation par les moteurs de recherche.
- Mise à jour des versions des dépendances de l'UI Kit.
- Correction de l'indentation des secrets dans les fichiers de déploiement.
- Ajout d'un rate limit global pour la sécurité.
