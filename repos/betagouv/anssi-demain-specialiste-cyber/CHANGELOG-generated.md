## Changelog : anssi-demain-specialiste-cyber (30 derniers jours, au 29 juillet 2026)

### Résumé
Ce mois-ci, le site a connu des améliorations significatives sur les pages "Cactus" et "Passe ton Hack d'abord" avec des ajustements de mise en page et de contenu pour une meilleure expérience utilisateur. Des améliorations de sécurité ont également été apportées au processus d'intégration continue et à la validation des configurations. Enfin, l'intégration du pixel de suivi Brevo pour la campagne "PIXEL" a été finalisée.

### Évolutions fonctionnelles
- **PIXEL :** Intégration du pixel de suivi Brevo pour enregistrer le consentement des utilisateurs. [#23d9c82](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/23d9c82)
- **Cactus :** Améliorations visuelles et de mise en page sur la page "Cactus", incluant le centrage d'éléments, la mise en italique de termes importants et l'amélioration de l'image de sensibilisation. [#c562bba](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/c562bba), [#adaa4cb](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/adaa4cb), [#2500966](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/2500966)
- **Passe ton Hack :** Ajustements de l'espacement de la marelle et centrage des étapes du challenge. [#d6fba65](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/d6fba65), [#ab61e88](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/ab61e88)
- **Passe ton Hack :** Modification du lien "Inscrire mes élèves" pour le rendre externe. [#0c0bf9f](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/0c0bf9f)
- **Webinaire CyberEnJeux :** Mise à jour de la bannière du webinaire. [#b9f5397](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/b9f5397)

### Évolutions techniques
- **Sécurité CI/CD :** Désactivation des identifiants git des dépôts clonés et validation des configurations pour renforcer la sécurité du pipeline CI/CD. [#7972f7d](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/7972f7d), [#0d77e09](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/0d77e09)
- **Sécurité :** Correction d'une vulnérabilité potentielle d'injection de code par 'template expansion'. [#096bae2](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/096bae2)
- **Dépendances :** Mise à jour de la dépendance `axios` pour corriger une faille de sécurité. [#2e85247](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/2e85247)
- **Pages Cactus et Passe ton Hack :** Création et implémentation des pages, incluant les différents modes d'affichage (desktop, tablette, mobile) et sections (présentation, avantages, témoignages, etc.). [#ae21346](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/ae21346), [#9da2d84](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/9da2d84)

### Autres changements
- **Documentation :** Ajout d'un skill pour l'intégration de landing page. [#fa82552](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/fa82552)
- **Mode élargi et Descriptions :** Réactivation du mode élargi et des descriptions. [#7026ed8](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/7026ed8), [#60d3584](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/60d3584)
- **Suppression d'une version d'exception :** Suppression de la version 1.15.0 des exceptions. [#ea0b6a5](https://github.com/betagouv/anssi-demain-specialiste-cyber/commit/ea0b6a5)
