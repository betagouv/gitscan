## Changelog : labonnealternance (30 derniers jours, au 02 octobre 2026)

### Résumé
Ce mois a été marqué par le lancement du MVP des "offres 100% libres", permettant une plus grande ouverture de la plateforme avec une modération assistée par IA. Un effort majeur a également été consacré à l'accessibilité numérique (RGAA) pour garantir une expérience inclusive sur l'ensemble des formulaires et parcours utilisateurs. Enfin, les capacités de recherche et de filtrage ont été significativement enrichies.

### Évolutions fonctionnelles
- **Nouveautés majeures** : Lancement du module d'offres totalement libres incluant un nouveau système de dépôt, une charte et une modération par IA ([#5078](https://github.com/mission-apprentissage/labonnealternance/issues/5078)).
- **Accessibilité (RGAA)** : Mise en conformité massive des formulaires (candidatures, simulateur, désinscription, back-office), des images, des icônes et de la navigation pour répondre aux critères d'accessibilité numérique ([#5621](https://github.com/mission-apprentissage/labonnealternance/issues/5621), [#5615](https://github.com/mission-apprentissage/labonnealternance/issues/5615), [#5600](https://github.com/mission-apprentissage/labonnealternance/issues/5600), [#5601](https://github.com/mission-apprentissage/labonnealternance/issues/5601), [#5622](https://github.com/mission-apprentissage/labonnealternance/issues/5622), [#5614](https://github.com/mission-apprentissage/labonnealternance/issues/5614), [#5580](https://github.com/mission-apprentissage/labonnealternance/issues/5580), [#5543](https://github.com/mission-apprentissage/labonnealternance/issues/5543), [#5511](https://github.com/mission-apprentissage/labonnealternance/issues/5511), [#5494](https://github.com/mission-apprentissage/labonnealternance/issues/5494), [#5483](https://github.com/mission-apprentissage/labonnealternance/issues/5483)).
- **Recherche et découverte** : 
    - Ajout de la recherche par département et région dans le champ lieu ([#5248](https://github.com/mission-apprentissage/labonnealternance/issues/5248)).
    - Création de pages dédiées aux diplômes (≤ bac+2) avec filtres par type d'école ([#5548](https://github.com/mission-apprentissage/labonnealternance/issues/5548)).
    - Intégration du flux LinkedIn pour enrichir les données ([#5482](https://github.com/mission-apprentissage/labonnealternance/issues/5482)).
- **Expérience utilisateur** :
    - Mise en place de la conservation des CV pendant un an avec purge automatique ([#5495](https://github.com/mission-apprentissage/labonnealternance/issues/5495)).
    - Ajout d'un motif de clôture d'offre ("J'ai reçu assez de candidatures") ([#5501](https://github.com/mission-apprentissage/labonnealternance/issues/5501)).
    - Diverses corrections d'affichage mobile et de comportement des formulaires de recherche et de candidature.
- **Modération** : Mise à jour de la liste noire des CFA ([#5475](https://github.com/mission-apprentissage/labonnealternance/issues/5475), [#5502](https://github.com/mission-apprentissage/labonnealternance/issues/5502)).

### Évolutions techniques
- **Architecture de recherche** : Refonte du moteur de recherche avec l'introduction d'une double écriture vers une nouvelle collection dédiée, optimisant la rapidité des suggestions et des résultats ([#5526](https://github.com/mission-apprentissage/labonnealternance/issues/5526), [#5525](https://github.com/mission-apprentissage/labonnealternance/issues/5525), [#5524](https://github.com/mission-apprentissage/labonnealternance/issues/5524)).
- **API** : 
    - Évolution de l'API v3 pour exposer de nouveaux champs (début de contrat, questions recruteurs) ([#5471](https://github.com/mission-apprentissage/labonnealternance/issues/5471)).
    - Création d'un endpoint batch pour les partenaires (liens RDV et recherche d'entreprises) ([#5562](https://github.com/mission-apprentissage/labonnealternance/issues/5562)).
- **Données et Sécurité** : 
    - Amélioration de l'anonymisation des candidatures ([#5516](https://github.com/mission-apprentissage/labonnealternance/issues/5516)).
    - Renforcement de l'obfuscation des données de test (seed) ([#5618](https://github.com/mission-apprentissage/labonnealternance/issues/5618)).
    - Migration vers le nouveau flux Hellowork ([#5223](https://github.com/mission-apprentissage/labonnealternance/issues/5223)).
- **CI/CD** : Automatisation du déclenchement de CodeQL lors de la phase de revue de code ([#5568](https://github.com/mission-apprentissage/labonnealternance/issues/5568)).

### Autres changements
- **Documentation et Process** : Alignement de la convention de nommage des Pull Requests et mise à jour des instructions pour les outils d'assistance IA (Claude/Copilot) ([#5522](https://github.com/mission-apprentissage/labonnealternance/issues/5522), [#5519](https://github.com/mission-apprentissage/labonnealternance/issues/5519)).
- **Nettoyage** : Suppression de templates inutilisés et de champs de données obsolètes ([#5644](https://github.com/mission-apprentissage/labonnealternance/issues/5644), [#5623](https://github.com/mission-apprentissage/labonnealternance/issues/5623)).
