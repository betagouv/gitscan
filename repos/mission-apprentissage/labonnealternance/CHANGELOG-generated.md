## Changelog : labonnealternance (30 derniers jours, au 07/10/2026)

### Résumé
Ce mois-ci a été marqué par le lancement majeur des "offres 100% libres" avec modération par IA et un effort intensif de mise en conformité pour l'accessibilité (RGAA 11). La plateforme a également bénéficié d'améliorations significatives sur ses outils de recherche, sa cartographie et son référencement naturel (SEO).

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** : 
    - Lancement du MVP des offres 100% libres incluant le dépôt, la charte et la modération par IA ([#5078](https://github.com/mission-apprentissage/labonnealternance/issues/5078)).
    - Intégration du flux LinkedIn ([#5482](https://github.com/mission-apprentissage/labonnealternance/issues/5482)).
    - Ajout de motifs de clôture d'offre pour les recruteurs ([#5501](https://github.com/mission-apprentissage/labonnealternance/issues/5501)).
- **Recherche et Découverte** :
    - Amélioration de la recherche par département et région ([#5248](https://github.com/mission-apprentissage/labonnealternance/issues/5248) ([#5461](https://github.com/mission-apprentissage/labonnealternance/issues/5461))).
    - Mise à jour de la cartographie des CFA ([#5660](https://github.com/mission-apprentissage/labonnealternance/issues/5660)).
    - Création de nouvelles pages dédiées aux diplômes (niveaux bac+2 et moins) ([#5605](https://github.com/mission-apprentissage/labonnealternance/issues/5605) ([#5548](https://github.com/mission-apprentissage/labonnealternance/issues/5548))).
- **Accessibilité (RGAA 11)** :
    - Mise en conformité massive des formulaires (connexion, création de compte, candidatures, simulateur, désinscription, réponses CFA et back-office) ([#5617](https://github.com/mission-apprentissage/labonnealternance/issues/5617) ([#5621](https://github.com/mission-apprentissage/labonnealternance/issues/5621) ([#5615](https://github.com/mission-apprentissage/labonnealternance/issues/5615) ([#5600](https://github.com/mission-apprentissage/labonnealternance/issues/5600) ([#5601](https://github.com/mission-apprentissage/labonnealternance/issues/5601) ([#5622](https://github.com/mission-apprentissage/labonnealternance/issues/5622) ([#5614](https://github.com/mission-apprentissage/labonnealternance/issues/5614))).
    - Corrections structurelles de l'HTML et des éléments obligatoires ([#5543](https://github.com/mission-apprentissage/labonnealternance/issues/5543) ([#5511](https://github.com/mission-apprentissage/labonnealternance/issues/5511)).
- **Expérience Utilisateur et Corrections** :
    - Optimisation du SEO via des méta-descriptions dynamiques et des titres de pages enrichis ([#5613](https://github.com/mission-apprentissage/labonnealternance/issues/5613) ([#5534](https://github.com/mission-apprentissage/labonnealternance/issues/5534))).
    - Mise en place d'une politique de conservation et de purge automatique des CV après un an ([#5495](https://github.com/mission-apprentissage/labonnealternance/issues/5495) ([#5518](https://github.com/mission-apprentissage/labonnealternance/issues/5518))).
    - Diverses corrections d'interface (affichage mobile, liens email, gestion des paramètres de recherche et saisie des métiers) ([#5632](https://github.com/mission-apprentissage/labonnealternance/issues/5632) ([#5578](https://github.com/mission-apprentissage/labonnealternance/issues/5578) ([#5590](https://github.com/mission-apprentissage/labonnealternance/issues/5590) ([#5508](https://github.com/mission-apprentissage/labonnealternance/issues/5508))).

### Évolutions techniques
- **Architecture et Performance** :
    - Refonte du système de recherche pour utiliser une collection dédiée par mode et suppression de la double écriture des données ([#5526](https://github.com/mission-apprentissage/labonnealternance/issues/5526) ([#5525](https://github.com/mission-apprentissage/labonnealternance/issues/5525) ([#5524](https://github.com/mission-apprentissage/labonnealternance/issues/5524))).
- **API et Backend** :
    - Évolution de l'API v3 pour exposer de nouveaux champs (début de contrat, questions recruteurs) ([#5471](https://github.com/mission-apprentissage/labonnealternance/issues/5471)).
    - Amélioration des endpoints pour les partenaires ([#5562](https://github.com/mission-apprentissage/labonnealternance/issues/5562)).
    - Optimisation de la gestion des données (anonymisation des candidatures, nettoyage des collections et du seed) ([#5516](https://github.com/mission-apprentissage/labonnealternance/issues/5516) ([#5618](https://github.com/mission-apprentissage/labonnealternance/issues/5618)).
- **CI/CD et Qualité** :
    - Automatisation des notifications de déploiement preview ([#5657](https://github.com/mission-apprentissage/labonnealternance/issues/5657)).
    - Intégration de CodeQL lors de la revue de code ([#5568](https://github.com/mission-apprentissage/labonnealternance/issues/5568)).
    - Amélioration du processus de publication des versions ([#5652](https://github.com/mission-apprentissage/labonnealternance/issues/5652)).

### Autres changements
- Mise à jour de la documentation technique et des instructions pour les outils d'IA (Claude/Copilot) ([#5519](https://github.com/mission-apprentissage/labonnealternance/issues/5519) ([#5522](https://github.com/mission-apprentissage/labonnealternance/issues/5522)).
- Nettoyage de la base de code (suppression de templates inutilisés et de commentaires obsolètes) ([#5644](https://github.com/mission-apprentissage/labonnealternance/issues/5644) ([#5521](https://github.com/mission-apprentissage/labonnealternance/issues/5521)).
