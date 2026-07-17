## Changelog : sante-mentale-etudiant (30 derniers jours, au 16 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la fonctionnalité "Trouver du soutien" avec l'ajout d'une page de résultats et l'amélioration de l'orientateur. Une première structure pour l'orientateur a été implémentée, ainsi qu'un premier bandeau d'accueil. Des améliorations techniques ont également été apportées à la configuration du projet, notamment la migration vers pnpm 11 et la configuration des jobs CI/CD.

### Évolutions fonctionnelles
- **Trouver du soutien :** Ajout d'une page de résultats pour l'orientateur [#10](https://github.com/betagouv/sante-mentale-etudiant/issues/10).
- **Trouver du soutien :** Liaison entre l'orientateur et la page de résultats.
- **Trouver du soutien :** Implémentation de filtres conditionnels.
- **Trouver du soutien :** Refactoring des filtres.
- **Trouver du soutien :** Amélioration du style (titre, sous-titre, padding, couleurs).
- **Orienteur :** Première structure et arbre de décision implémentés [#6](https://github.com/betagouv/sante-mentale-etudiant/issues/6).
- **Page d'accueil :** Ajout d'un premier bandeau [#1](https://github.com/betagouv/sante-mentale-etudiant/issues/1).
- **UI :** Ajout d'un composant de carte personnalisé.
- **UI :** Correction de l'espacement mobile de l'orientateur.
- **UI :** Correction de la hauteur de l'image de l'orientateur.
- **UI :** Définition du thème par défaut sur le mode clair.

### Évolutions techniques
- **CI/CD :** Initialisation des jobs GitHub CI/CD [#5](https://github.com/betagouv/sante-mentale-etudiant/pull/5).
- **Gestion des dépendances :** Migration vers pnpm 11.
- **Gestion des dépendances :** Correction de la configuration pnpm pour les overrides.
- **Gestion des dépendances :** Approbation des scripts de build pnpm pour le déploiement.
- **Sécurité :** Correction d'une vulnérabilité postcss avec pnpm audit.

### Autres changements
- Correction de noms de couleurs dans le code.
- Nettoyage des noms de couleurs.
- Correction d'une erreur de clé.
- Correction d'un bug dans "Trouver du soutien".
