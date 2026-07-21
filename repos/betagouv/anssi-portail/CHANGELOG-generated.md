## Changelog : anssi-portail (30 derniers jours, au 20 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations techniques, notamment la migration vers le rendu côté serveur (SSR) pour de nombreuses pages, améliorant ainsi la performance et le SEO. Des corrections et des améliorations ont également été apportées à l'expérience utilisateur, en particulier concernant le parcours de sécurisation et la gestion des financements. Des efforts ont été faits pour renforcer la sécurité et la conformité du site.

### Évolutions fonctionnelles
- Implémentation du suivi du consentement aux données via un pixel ([c172c26](https://github.com/betagouv/anssi-portail/commit/c172c26)).
- Amélioration de l'affichage et de la navigation dans le parcours de sécurisation, avec notamment l'ajout de barres de progression et de badges de complétion ([b4b4b57](https://github.com/betagouv/anssi-portail/commit/b4b4b57), [e7ebce3](https://github.com/betagouv/anssi-portail/commit/e7ebce3), [a910ee4](https://github.com/betagouv/anssi-portail/commit/a910ee4)).
- Correction de bugs et amélioration de l'affichage des pages "Financements" et "Collectivités" ([82d2d08](https://github.com/betagouv/anssi-portail/commit/82d2d08), [87e8e87](https://github.com/betagouv/anssi-portail/commit/87e8e87)).
- Ajout de données structurées pour améliorer l'indexation SEO ([9abfb44](https://github.com/betagouv/anssi-portail/commit/9abfb44)).
- Amélioration de l'affichage des cartes et des composants DSFR ([711808f](https://github.com/betagouv/anssi-portail/commit/711808f), [ee27bfc](https://github.com/betagouv/anssi-portail/commit/ee27bfc)).

### Évolutions techniques
- Migration de nombreuses pages vers le rendu côté serveur (SSR) pour améliorer la performance et le SEO (pages des associations, financements, NIS2, guides, etc.) ([d5dbe38](https://github.com/betagouv/anssi-portail/commit/d5dbe38), [77ba019](https://github.com/betagouv/anssi-portail/commit/77ba019), [26d4020](https://github.com/betagouv/anssi-portail/commit/26d4020)).
- Refonte de l'architecture pour faciliter l'enrichissement des composants Svelte ([7c026c5](https://github.com/betagouv/anssi-portail/commit/7c026c5), [3f1f40c](https://github.com/betagouv/anssi-portail/commit/3f1f40c)).
- Mise à jour de nombreuses dépendances (Vitest, Prettier, CSSNano, etc.).
- Amélioration de la configuration CI/CD et des secrets.
- Ajout d'un shell Nix pour faciliter le développement en local ([a02ad43](https://github.com/betagouv/anssi-portail/commit/a02ad43)).
- Renforcement de la sécurité avec l'ajout d'outils d'analyse (zizmor) et la correction de vulnérabilités potentielles ([9d3965f](https://github.com/betagouv/anssi-portail/commit/9d3965f)).

### Autres changements
- Ajout de tests et amélioration de la couverture de tests.
- Documentation mise à jour.
- Nettoyage du code et refactoring de certains composants.
- Ajout de métadonnées Open Graph et Twitter pour améliorer le partage sur les réseaux sociaux ([1718051](https://github.com/betagouv/anssi-portail/commit/1718051)).
- Correction de styles et d'éléments d'interface utilisateur mineurs.
- Ajout d'un composant "Tuile" en Svelte ([38e0c2a](https://github.com/betagouv/anssi-portail/commit/38e0c2a)).
