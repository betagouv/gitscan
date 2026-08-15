## Changelog : sante-mentale-etudiant (30 derniers jours, au 14 août 2026)

### Résumé
Ce mois a été marqué par une structuration importante du contenu et de l'interface. La plateforme s'enrichit de fonctionnalités clés comme un système d'articles complet, une section dédiée aux ressentis, une page d'aide pour l'entourage, ainsi qu'un module d'inscription à la newsletter. L'expérience utilisateur est également améliorée par une navigation plus fluide et une meilleure adaptation aux supports mobiles.

### Évolutions fonctionnelles
- **Enrichissement de la page d'accueil** : Ajout de nouvelles sections incluant une grille de ressentis, des statistiques et une bannière d'appel à l'aide.
- **Système d'articles** : Mise en place d'un template d'article complet incluant le temps de lecture, des thématiques liées et un support pour le contenu en Markdown [#25](https://github.com/betagouv/sante-mentale-etudiant/pull/25).
- **Section "Ressentis"** : Développement d'une interface dédiée comprenant une FAQ, des conseils et une gestion de la réactivité [#27](https://github.com/betagouv/sante-mentale-etudiant/pull/27).
- **Nouvelles pages et modules** :
    - Création de la page "Aider un proche".
    - Intégration d'un module de newsletter avec connexion à l'API Brevo [#22](https://github.com/betagouv/sante-mentale-etudiant/pull/22).
    - Amélioration du pied de page (mentions légales, liens de navigation).
- **Outils d'orientation et de soutien** :
    - Amélioration de l'affichage des résultats et des modales pour l'outil d'orientation [#10](https://github.com/betagouv/sante-mentale-etudiant/pull/10) [#23](https://github.com/betagouv/sante-mentale-etudiant/pull/23).
    - Corrections de bugs sur la recherche de soutien "Près de chez toi" [#20](https://github.com/betagouv/sante-mentale-etudiant/pull/20) [#21](https://github.com/betagouv/sante-mentale-etudiant/pull/21).

### Évolutions techniques
- **Gestion de contenu** : Installation et configuration de `remark` et `remark-html` pour le rendu des articles en Markdown.
- **Optimisation de la navigation** : Remplacement des balises `<a>` par les composants `<Link>` de Next.js pour améliorer la fluidité de navigation.
- **Refactoring et architecture** :
    - Réorganisation de la structure de la page d'accueil et des composants d'articles.
    - Mise en place de la gestion des adresses API [#11](https://github.com/betagouv/sante-mentale-etudiant/pull/11).
- **Interface et Design** :
    - Amélioration globale de la réactivité (responsive design) sur les pages articles, ressentis et aide.
    - Ajustements typographiques et de mise en page pour les écrans mobiles.

### Autres changements
- **Maintenance du code** : Harmonisation du nommage des pages et nettoyage des variables de couleurs.
- **Organisation** : Réorganisation des fichiers et mise à jour de la documentation interne.
