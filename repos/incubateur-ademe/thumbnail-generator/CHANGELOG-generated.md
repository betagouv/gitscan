## Changelog : thumbnail-generator (30 derniers jours)

### Résumé
Le générateur de vignettes a été entièrement retravaillé et est désormais fonctionnel. Cette version initiale permet de créer des vignettes SVG et PNG personnalisées avec un titre, un sous-titre, une date et un logo. L'interface a été modernisée et inclut un mode sombre, une exportation PNG et un aperçu du code SVG. Un workflow de déploiement automatique vers GitHub Pages a également été mis en place.

### Évolutions fonctionnelles
- Ajout de l'interface utilisateur avec une barre latérale redimensionnable, une section de logo repensée, un code SVG repliable et un bouton de fermeture pour les presets (#b1d6873)
- Implémentation de l'exportation des vignettes au format PNG (#98a6605)
- Ajout d'un aperçu du code SVG généré (#98a6605)
- Ajout du support du mode sombre/clair (#98a6605)
- Correction d'un problème de résolution des URL des SVG des presets en préfixant avec `BASE_URL` (#d9b71a2)
- Correction d'une faute de frappe dans le chemin de base (`thumbail` -> `thumbnail`) (#6261aac)

### Évolutions techniques
- Initialisation du projet avec Vite, React 19 et TypeScript (#4a97cf2)
- Mise à jour vers Tailwind CSS v4 et intégration de shadcn/ui (new-york) (#630c183)
- Ajout de la gestion d'état des vignettes et des presets (#a2d904d)
- Implémentation d'un canvas SVG (1280x720) avec intégration des polices et rendu du logo (#21c4baa)
- Ajout de composants de contrôle (#af934d3)
- Ajout d'un layout d'application (#98a6605)
- Mise en place d'un workflow GitHub Actions pour le déploiement sur GitHub Pages (#15881d5)
- Configuration de ESLint v10, Prettier et .gitignore pour la qualité du code (#ebcda45)

### Autres changements
- Ajout d'un fichier README, d'une licence MIT et d'un fichier CLAUDE.md (#0fb2950)
- Documentation des compétences de l'agent (#0fb2950)
- Ajout d'une compétence webdesign (#47e7442)
