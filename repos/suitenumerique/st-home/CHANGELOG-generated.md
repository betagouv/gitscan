## Changelog : st-home (30 derniers jours, au 29 mai 2026)

### Résumé
Cette mise à jour apporte des corrections et améliorations concernant la recherche de communes, l'affichage de la carte de déploiement, la gestion des services et la présentation des informations sur les collectivités. L'intégration du centre d'aide a également été mise à jour et des corrections de style ont été apportées au CMS.

### Évolutions fonctionnelles
- **Recherche de communes :** Correction pour inclure les organisations ayant un nom exact lors de la recherche. [#69](https://github.com/suitenumerique/st-home/issues/69)
- **Carte de déploiement :**
    - Correction de l'affichage des seuils sur la carte de déploiement.
    - Prise en compte correcte des seuils dans le calcul de la carte.
    - Amélioration de l'affichage des régions et départements sur la carte. [#65](https://github.com/suitenumerique/st-home/issues/65)
- **Services :** Correction pour éviter la duplication des services ProConnect dans la liste.
- **Centre d'aide :** Mise à jour du lien vers le centre d'aide. [#67](https://github.com/suitenumerique/st-home/issues/67)
- **RPNT :** Autorisation de certains redirects vers des sites gouv. [#69](https://github.com/suitenumerique/st-home/issues/69)

### Évolutions techniques
- **Données :** Passage à la nouvelle URL de Banatic.
- **CMS :** Mise à jour vers la dernière version de Docs et correction des styles pour les blocs de citation et les résumés.
- **CMS :** Assouplissement de la détection du frontmatter.

### Autres changements
- Restauration du bloc de service ANCT de secours dans la page d'accueil.
