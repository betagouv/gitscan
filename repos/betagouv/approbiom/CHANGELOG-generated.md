## Changelog : approbiom (30 derniers jours, au 26 mai 2026)

### Résumé
Ce changelog marque les débuts du projet approbiom, une initiative visant à créer des widgets personnalisés pour Grist. Les premiers développements se concentrent sur la mise en place de l'infrastructure de build et la création d'un widget de carte simple. Le projet est maintenant déployable sur GitHub Pages.

### Évolutions fonctionnelles
- Création d'un widget de carte simple [#1](https://github.com/betagouv/approbiom/pulls/1) (b9833a9)
- Mise en place de la structure de base pour les widgets Grist utilisant Vite en mode MPA (Multiple Page Application) (608ffd9)

### Évolutions techniques
- Configuration du build pour déployer les widgets dans le dossier `docs/` pour GitHub Pages (f07c321)
- Ajout d'un workflow GitHub Actions pour automatiser le build et le déploiement sur GitHub Pages (ade3700)
- Contournement des politiques de sécurité de pnpm pour permettre le build en CI (79f57ed, 907179a, d30852d)
- Renommage du dossier `grist-widgets` en `grist-widget` pour plus de clarté (bd63757)
- Initialisation du projet et configuration initiale (72c841c, d57bd82)
- Formatage des fichiers grist-widget (b01bbc0)
- Ajout d'un fichier `.nojekyll` pour éviter que Jekyll n'interfère avec les assets préfixés par un underscore (38a350d)

### Autres changements
- Aucun changement significatif à signaler dans cette catégorie.
